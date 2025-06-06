
from controladores.bd import obtener_conexion , sql_select_fetchall , sql_select_fetchone , sql_execute , sql_execute_lastrowid , show_columns , show_primary_key , exists_column_Activo , unactive_row_table
import controladores.bd as bd


table_name = 'categoria'

def get_info_columns():
    return show_columns(table_name)


def get_primary_key():
    return show_primary_key(table_name)


def exists_Activo():
    return exists_column_Activo(table_name)


def delete_row( id ):
    sql = f'''
        delete from {table_name}
        where id = {id}
    '''
    sql_execute(sql)


#####_ CAMBIAR SQL y DICT INTERNO _#####

def table_fetchall():
    sql= f'''
        select 
            *
        from {table_name}
    '''
    resultados = sql_select_fetchall(sql)
    
    return resultados


def get_table():
    sql= f'''
        select 
            tip.id ,
            tip.nombre ,
            tip.descripcion ,
            tip.activo 
        from {table_name} tip
    '''
    columnas = {
        'id': ['ID' , 0.5] , 
        'nombre' : ['Nombre' , 4.5] , 
        'descripcion' : ['Descripción' , 4.5] , 
        'activo' : ['Actividad' , 1] 
        }
    filas = sql_select_fetchall(sql)
    
    return columnas , filas


######_ CRUD ESPECIFICAS _###### 

def unactive_row( id ):
    unactive_row_table(table_name , id)


def insert_row( nombre , descripcion=None ):
    sql = f'''
        INSERT INTO 
            {table_name} 
            ( nombre , descripcion , activo )
        VALUES 
            ( %s , %s , 1 )
    '''
    sql_execute(sql,( nombre , descripcion ))


def update_row( id , nombre , descripcion ):
    sql = f'''
        update {table_name} set 
        nombre = %s ,
        descripcion = %s
        where {get_primary_key()} = {id}
    '''
    sql_execute(sql, (nombre , descripcion ))


#####_ ADICIONALES _#####

def get_options():
    sql= f'''
        select 
            id,
            nombre
        from {table_name}
        order by nombre asc
    '''
    filas = sql_select_fetchall(sql)
    
    lista = [(fila['id'], fila["nombre"]) for fila in filas]

    return lista


def obtener_categorias():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM CATEGORIA WHERE activo = 1")
        resultado = cursor.fetchall()
    conexion.close()
    return resultado

