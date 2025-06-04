# import pymysql
# from pymysql.cursors import DictCursor
import requests

def request_api_sql( tipo , sql, args= None ):
    try:
        res = requests.post("https://franckcv.pythonanywhere.com/api/sql", json={
            "tipo": tipo ,
            "sql": sql ,
            "args": args
        })
        return res.json()
    except Exception as e:
        return e


def sql_select_fetchall(sql , args = None):
    return request_api_sql( 'fetchall' , sql , args )


def sql_select_fetchone(sql , args = None):
    return request_api_sql( 'fetchone' , sql , args )


def sql_execute(sql , args = None):
    return request_api_sql( 'execute' , sql , args )


def sql_execute_lastrowid(sql , args = None):
    return request_api_sql( 'execute_last_id' , sql , args )





