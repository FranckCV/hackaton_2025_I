import controladores.bd as bd
import json
from datetime import datetime, date , timedelta
import pytz
import gpt_utils as gpt
import ast

def local_hour():
    return datetime.now(pytz.utc).astimezone(pytz.timezone('America/Lima'))


def insert_data_webhook( data , fecha = None):
    sql = f'''
        INSERT INTO
            webhook
            ( dato , fecha )
        VALUES
            ( %s , %s )
    '''
    bd.sql_execute(sql,( json.dumps(data) , fecha ))


def insert_data_webhook_lastid( data , fecha = None):
    sql = f'''
        INSERT INTO
            webhook
            ( dato , fecha )
        VALUES
            ( %s , %s )
    '''
    bd.sql_execute_lastrowid(sql,( json.dumps(data) , fecha ))


def get_table():
    sql= f'''
        select
            id ,
            fecha,
            dato
        from webhook
        order by 1 desc
    '''
    filas = bd.sql_select_fetchall(sql)

    return filas


def limpiar_estados_expirados():
    ahora = local_hour()
    limite = ahora - timedelta(minutes=10)

    sql = """
        DELETE FROM estado_usuario
        WHERE ultima_interaccion < %s
    """
    bd.sql_execute(sql, [limite])


def set_estado(numero, estado, categoria_id=None):
    sql ='''
        INSERT INTO estado_usuario (numero, estado, categoriaid, ultima_interaccion)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE estado=%s, categoriaid=%s, ultima_interaccion=%s
    '''
    now = local_hour()
    bd.sql_execute(sql, (numero, estado, categoria_id, now, estado, categoria_id, now))


def get_estado(numero):
    sql ='''
        SELECT estado FROM estado_usuario WHERE numero = %s
    '''
    row = bd.sql_select_fetchone(sql,(numero,))
    return row["estado"] if row else None


def get_categoria_actual(numero):
    row = bd.sql_select_fetchone("SELECT categoriaid FROM estado_usuario WHERE numero = %s", (numero,))
    return row["categoriaid"] if row else None


def limpiar_estado(numero):
    bd.sql_execute("DELETE FROM estado_usuario WHERE numero = %s", (numero,))


def get_categorias():
    sql= f'''
        select
            id ,
            nombre
        from categoria
        where activo = 1
        order by 2 asc
    '''
    filas = bd.sql_select_fetchall(sql)

    return filas


def get_preguntas_por_categoria(categoria_id):
    rows = bd.sql_select_fetchall("SELECT id, titulo FROM pregunta WHERE CATEGORIAid = %s", (categoria_id,))
    return rows


def get_respuesta_por_id(pregunta_id):
    row = bd.sql_select_fetchone("SELECT respuesta FROM pregunta WHERE id = %s", (pregunta_id,))
    return row["respuesta"] if row else "No encontré esa pregunta."


def buscar_pregunta_en_categoria(texto, categoria_id):
    sql = """
        SELECT respuesta
        FROM pregunta
        WHERE CATEGORIAid = %s AND LOWER(titulo) LIKE %s
        LIMIT 1
    """
    row = bd.sql_select_fetchone(sql, (categoria_id, f"%{texto.lower()}%"))
    return row["respuesta"] if row else "Lo siento, no encontré una respuesta relacionada a eso."


def buscar_respuesta_similar(texto):
    sql = """
        SELECT respuesta
        FROM pregunta
        WHERE LOWER(titulo) LIKE %s
        LIMIT 1
    """
    row = bd.sql_select_fetchone(sql, (f"%{texto.lower()}%",))
    return row["respuesta"] if row else "Lo siento, no tengo una respuesta exacta, pero puedes preguntar de otra forma."


def responder_gpt_con_texto_libre(texto_usuario , fecha ):
    sql = """
        SELECT p.titulo, p.respuesta
        FROM pregunta p
        LEFT JOIN palabra_clave pk ON pk.preguntaid = p.id

    """
    # like = f"%{texto_usuario.lower()}%"
    ejemplos = bd.sql_select_fetchall(sql)
    return gpt.responder_con_gpt_modo_abierto(texto_usuario, ejemplos , fecha )


def responder_gpt_desde_pregunta(pregunta_id):
    sql = "SELECT titulo, respuesta FROM pregunta WHERE id = %s"
    pregunta = bd.sql_select_fetchone(sql, [pregunta_id])
    if not pregunta:
        return "Lo siento, no encontré la información solicitada."
    prompt = (
        f"Pregunta: {pregunta['titulo']}\n"
        f"Respuesta oficial: {pregunta['respuesta']}\n\n"
        "Esta es la respuesta a la pregunta que se encuentra en labase de datos. Responde al usuario con amabilidad y profesionalismo. No es necesario que saludes"
    )
    return gpt.ejecutar_prompt_usat(prompt)


def obtener_documentos_relacionados(texto):
    sql = """
        SELECT * FROM documento
        WHERE activo = 1 AND (
            LOWER(titulo) LIKE %s OR
            LOWER(descripcion) LIKE %s
        )
        LIMIT 2
    """
    like = f"%{texto.lower()}%"
    return bd.sql_select_fetchall(sql, [like, like])


def responder_gpt_con_doc_soporte(texto_usuario, fecha ):
    # 1. Buscar preguntas relacionadas
    sql_preg = """
        SELECT p.titulo, p.respuesta
        FROM pregunta p
        LEFT JOIN palabra_clave pk ON pk.preguntaid = p.id
    """
    ejemplos = bd.sql_select_fetchall(sql_preg)

    sql_docs = """
        SELECT titulo, url, descripcion
        FROM documento
        WHERE activo = 1
    """
    docs = bd.sql_select_fetchall(sql_docs)

    # 3. Construir el prompt
    prompt = f"El usuario ha preguntado: \"{texto_usuario}\"\n\nBase de datos de respuestas:\n"
    for i, ej in enumerate(ejemplos, 1):
        prompt += f"{i}. {ej['titulo']} → {ej['respuesta']}\n"

    if docs:
        prompt += "\n📎 Documentos disponibles:\n"
        for doc in docs:
            prompt += f"{doc}\n"

        prompt += (
            "\nSi alguno de estos documentos puede complementar la respuesta, "
            "menciónalo y sugiere al usuario que lo revise. No es necesario que siempre sugieras un documento y hables a profundidad de su descripción , solo lo importante que pueda responder la pregunta"
        )

    prompt2 = prompt + "\n\nDe la lista de documentos analizados devuelveme solo los diccionarios presentados que realmente respondan a la pregunta en una lista []. No des explicaciones, solo envia los diccionarios con los mismos elementos en una lista [], sean varios, uno o ninguno"
    docs_str = gpt.ejecutar_prompt_usat(prompt2)
    docs_lst = ast.literal_eval(docs_str)

    prompt += "\n\nResponde de forma clara, amable y profesional usando esta información."
    respuesta = gpt.ejecutar_prompt_usat(prompt)

    # 5. Verificar si la respuesta fue útil
    fue_util = gpt.verificar_si_gpt_respondio(texto_usuario, respuesta)

    if str(fue_util) == "0":
        bd.insert_data_historial(texto_usuario, fecha)

    return respuesta, docs_lst




# respuesta_s, docs_s = responder_gpt_con_doc_soporte('pasame el plan de estudios nuevo de este año', '2025-06-05' )


# print(respuesta_s)
# print("---------------------")
# print(docs_s)

