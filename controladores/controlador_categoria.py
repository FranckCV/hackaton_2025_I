from controladores.bd import obtener_conexion

def obtener_categorias():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM CATEGORIA WHERE activo = 1")
        resultado = cursor.fetchall()
    conexion.close()
    return resultado
