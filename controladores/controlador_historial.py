from controladores.bd import obtener_conexion, sql_select_fetchall, sql_select_fetchone, sql_execute, sql_execute_lastrowid, show_columns, show_primary_key, exists_column_Activo, unactive_row_table

import controladores.bd as bd

#####_ CONFIGURACIÓN PRINCIPAL _#####

table_name = 'historial'

def get_info_columns():
    return show_columns(table_name)

def get_primary_key():
    return show_primary_key(table_name)

def exists_Activo():
    return False

def delete_row(id):
    bd.delete_row_table(table_name, id)

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
        LEFT JOIN categoria c ON c.id = h.categoriaid
        ORDER BY h.fecha DESC
    '''
    columnas = {
        'id': ['ID', 0.3],
        'mensaje': ['Mensaje', 3],
        'fecha': ['Fecha', 2],
        'estado': ['Estado', 1],
        'categoria': ['Categoría', 1.5],
    }
    filas = sql_select_fetchall(sql)
    return columnas, filas

def unactive_row(id):
    pass

def insert_row(mensaje, estado, categoriaid=None):
    sql = f'''
        INSERT INTO historial (mensaje, estado, categoriaid)
        VALUES (%s, %s, %s)
    '''
    sql_execute(sql, (mensaje, estado, categoriaid))

def update_row(id, mensaje, estado, categoriaid=None):
    sql = f'''
        UPDATE historial SET
        mensaje = %s,
        estado = %s,
        categoriaid = %s
        WHERE id = %s
    '''
    sql_execute(sql, (mensaje, estado, categoriaid, id))

def get_options():
    sql = f'''
        SELECT id, mensaje
        FROM historial
        ORDER BY fecha DESC
    '''
    filas = sql_select_fetchall(sql)
    return [(fila['id'], fila["mensaje"]) for fila in filas]