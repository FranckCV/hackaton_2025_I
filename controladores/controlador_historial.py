from controladores.bd import obtener_conexion, sql_select_fetchall, sql_select_fetchone, sql_execute, sql_execute_lastrowid, show_columns, show_primary_key, exists_column_Activo, unactive_row_table

import controladores.bd as bd

#####_ CONFIGURACIÓN PRINCIPAL _#####

table_name = 'historial'

def get_info_columns():
    return show_columns(table_name)

def get_primary_key():
    return show_primary_key(table_name)

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
            h.estado,
            c.nombre AS categoria
        FROM historial h
        LEFT JOIN categoria c ON h.categoriaid = c.id
        ORDER BY h.fecha DESC
    '''
    columnas = {
        'id': ['ID', 0.5],
        'mensaje': ['Mensaje', 4],
        'fecha': ['Fecha', 2],
        'estado': ['Estado', 1],
        'categoria': ['Categoría', 2]
    }
    filas = sql_select_fetchall(sql)
    return columnas, filas

def insert_historial(mensaje, estado=1, categoriaid=None):
    sql = f'''
        INSERT INTO {table_name} (mensaje, estado, categoriaid)
        VALUES (%s, %s, %s)
    '''
    sql_execute(sql, (mensaje, estado, categoriaid))

def get_ultimos(n=10):
    sql = f'''
        SELECT 
            h.mensaje,
            h.fecha,
            h.estado,
            c.nombre AS categoria
        FROM historial h
        LEFT JOIN categoria c ON h.categoriaid = c.id
        ORDER BY h.fecha DESC
        LIMIT %s
    '''
    return sql_select_fetchall(sql, (n,))