
from controladores.bd import obtener_conexion, delete_row_table, sql_select_fetchall, sql_select_fetchone, sql_execute, sql_execute_lastrowid, show_columns, show_primary_key, exists_column_Activo, unactive_row_table

#####_ CONFIGURACIÓN PRINCIPAL _#####

import controladores.bd as bd

table_name = 'historial'

def get_info_columns():
    return show_columns(table_name)

def get_primary_key():
    return show_primary_key(table_name)

def exists_Activo():
    return True

def delete_row(id):
    bd.delete_row_table(table_name, id)

def unactive_row(id):
    sql = f'''
        UPDATE {table_name}
        SET activo = NOT activo
        WHERE {get_primary_key()} = %s
    '''
    sql_execute(sql, [id])

def table_fetchall():
    sql = f'''
        SELECT *
        FROM {table_name}
    '''
    return sql_select_fetchall(sql)

def get_table():
    sql = f'''
        SELECT 
            h.id,
            h.mensaje,
            h.fecha,
            h.activo
        FROM historial h
        ORDER BY h.fecha DESC
    '''
    columnas = {
        'id': ['ID', 0.3],
        'mensaje': ['Mensaje', 3],
        'fecha': ['Fecha', 2],
        'activo': ['Estado', 1],
    }
    filas = sql_select_fetchall(sql)
    return columnas, filas

def insert_row(mensaje, activo=0):
    sql = f'''
        INSERT INTO {table_name} (mensaje, activo)
        VALUES (%s, %s)
    '''
    sql_execute(sql, (mensaje, activo))

def update_row(id, mensaje, activo):
    sql = f'''
        UPDATE {table_name}
        SET mensaje = %s,
            activo = %s
        WHERE id = %s
    '''
    sql_execute(sql, (mensaje, activo, id))

def get_options():
    sql = f'''
        SELECT id, mensaje
        FROM {table_name}
        ORDER BY fecha DESC
    '''
    filas = sql_select_fetchall(sql)
    return [(fila['id'], fila["mensaje"]) for fila in filas]




def get_report_test():
    sql = f'''
        SELECT 
            h.id,
            h.mensaje,
            h.fecha,
            h.activo
        FROM historial h
        ORDER BY h.fecha DESC
    '''
    columnas = {
        'id': ['ID', 0.5],
        'mensaje': ['Mensaje', 2],
        'fecha': ['Fecha', 1.5],
        'activo': ['Estado', 1],
    }
    filas = sql_select_fetchall(sql)
    return columnas, filas

def get_data():
    sql = f'''
        SELECT 
            h.mensaje,
            h.fecha
        FROM historial h
        ORDER BY h.fecha DESC
    '''
    filas = sql_select_fetchall(sql)
    return filas

def get_question_count():
    sql = '''
        SELECT COUNT(*) AS cantidad_historial FROM historial
    '''
    resultado = sql_select_fetchall(sql)
    return resultado[0]['cantidad_historial'] if resultado else 0
