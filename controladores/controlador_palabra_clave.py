from controladores.bd import obtener_conexion , sql_select_fetchall , sql_select_fetchone , sql_execute , sql_execute_lastrowid , show_columns , show_primary_key , exists_column_Activo , unactive_row_table
import controladores.bd as bd
#####_ MANTENER IGUAL - SOLO CAMBIAR table_name _#####

table_name = 'palabra_clave'

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
            pa.palabra ,
            p.titulo as titulo_pre 
        from {table_name} pa
        inner join pregunta p on p.id = pa.preguntaid
        order by pa.id asc
    '''
    columnas = {
        'id': ['ID' , 0.5 ] , 
        'palabra' : ['Palabra' , 3] , 
        'titulo_pre' : ['Pregunta' , 3],
    }
    filas = sql_select_fetchall(sql)
    
    return columnas , filas


######_ CRUD ESPECIFICAS _###### 

def unactive_row(id):
    unactive_row_table({table_name}, id)


def insert_row(palabra , preguntaid):
    sql = f'''
        INSERT INTO 
            palabra_clave (palabra,preguntaid) 
        VALUES 
            (%s, %s, %s)
    '''
    sql_execute(sql, (palabra , preguntaid))


def update_row(palabra, preguntaid, id):
    sql = f'''
        UPDATE {table_name} SET 
            palabra = %s,
            preguntaid = %s
        where {get_primary_key()} = {id}
    '''
    sql_execute(sql, (palabra,preguntaid))


#####_ ADICIONALES _#####

def get_options():
    sql= f'''
        SELECT 
            id,
            palabra
        FROM {table_name}
        where activo = 1
        ORDER BY palabra asc
    '''
    filas = sql_select_fetchall(sql)
    
    lista = [(fila[get_primary_key()], fila['palabra']) for fila in filas]

    return lista
