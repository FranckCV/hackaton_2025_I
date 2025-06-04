from controladores.bd import obtener_conexion

def buscar_respuesta_por_palabra(mensaje):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = """
        SELECT p.respuesta, COUNT(*) AS coincidencias
        FROM PREGUNTA p
        JOIN PALABRA_CLAVE pk ON pk.PREGUNTAid = p.id
        WHERE %s LIKE CONCAT('%%', pk.palabra, '%%')
        GROUP BY p.id
        ORDER BY coincidencias DESC
        LIMIT 1
        """
        cursor.execute(consulta, (mensaje,))
        resultado = cursor.fetchone()
    conexion.close()
    return resultado['respuesta'] if resultado else None

def obtener_preguntas_por_categoria(categoria_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT titulo FROM PREGUNTA WHERE CATEGORIAid = %s", (categoria_id,))
        resultado = cursor.fetchall()
    conexion.close()
    return resultado

def obtener_respuesta_por_titulo(titulo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT respuesta FROM PREGUNTA WHERE titulo = %s", (titulo,))
        resultado = cursor.fetchone()
    conexion.close()
    return resultado['respuesta'] if resultado else None
