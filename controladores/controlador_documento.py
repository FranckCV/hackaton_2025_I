
from controladores.bd import obtener_conexion , sql_select_fetchall , sql_select_fetchone , sql_execute , sql_execute_lastrowid , show_columns , show_primary_key , exists_column_Activo , unactive_row_table
import controladores.bd as bd

table_name = 'documento'

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
            pa.id ,
            pa.titulo ,
            pa.descripcion,
            pa.url,
            # pa.activo,
            p.titulo as titulo_pre 
        from {table_name} pa
        left join pregunta p on p.id = pa.preguntaid
        order by p.id asc
    '''
    columnas = {
        'id': ['ID' , 0.5 ] , 
        'titulo' : ['titulo' , 2] , 
        # 'descripcion' : ['descripcion' , 3] , 
        'url' : ['url' , 2] , 
        # 'activo' : ['activo' , 1] , 
        'titulo_pre' : ['Pregnta' , 2],
    }
    filas = sql_select_fetchall(sql)
    
    return columnas , filas


######_ CRUD ESPECIFICAS _###### 

def unactive_row(id):
    unactive_row_table({table_name}, id)


def insert_row(titulo, descripcion ,url, preguntaid):
    sql = f'''
        INSERT INTO 
            documento (titulo,descripcion,url,preguntaid,activo) 
        VALUES 
            (%s, %s, %s,%s,1)
    '''
    sql_execute(sql, (titulo, descripcion ,url, preguntaid))


def update_row(titulo, descripcion, url,preguntaid, id):
    sql = f'''
        UPDATE {table_name} SET 
            titulo = %s,
            descripcion =%s,
             url =%s,
            preguntaid = %s
        where {get_primary_key()} = {id}
    '''
    sql_execute(sql, (titulo, descripcion,url,preguntaid))


#####_ ADICIONALES _#####

def get_options():
    sql= f'''
        SELECT 
            id,
            titulo
        FROM {table_name}
        ORDER BY titulo asc
    '''
    filas = sql_select_fetchall(sql)
    
    lista = [(fila[get_primary_key()], fila['titulo']) for fila in filas]

    return lista
