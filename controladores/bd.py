import pymysql
from pymysql.cursors import DictCursor

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                port=3306,
                                # port=3307,
                                user='root',
                                password='',
                                db='bd_chatbot' ,                                
                                cursorclass=DictCursor
                                )


