
from controladores.bd import obtener_conexion , sql_select_fetchall , sql_select_fetchone , sql_execute , sql_execute_lastrowid , show_columns , show_primary_key , exists_column_Activo , unactive_row_table
import controladores.bd as bd

def get_user_count():
    sql = '''
        SELECT COUNT(*) AS cantidad_usuarios FROM estado_usuario
    '''
    resultado = sql_select_fetchall(sql)
    return resultado[0]['cantidad_usuarios'] if resultado else 0
