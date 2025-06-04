from controladores.bd import obtener_conexion

def buscar_respuesta_por_palabra(mensaje):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = """
        SELECT DISTINCT p.respuesta
        FROM PREGUNTA p
        JOIN PALABRA_CLAVE pk ON pk.PREGUNTAid = p.id
        WHERE %s LIKE CONCAT('%', pk.palabra, '%')
        LIMIT 1;
        """
        cursor.execute(consulta, (mensaje,))
        resultado = cursor.fetchone()
    conexion.close()
    return resultado['respuesta'] if resultado else None
