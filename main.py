from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for

import controladores.controlador_pregunta as controlador_pregunta
import controladores.controlador_categoria as controlador_categoria
import modelo_semantico
import os
import requests
from datetime import datetime, date
import hashlib
import base64

# load_dotenv()

app = Flask(__name__, template_folder='templates')

STATE_0              = configuraciones.STATE_0
STATE_1              = configuraciones.STATE_1
TITLE_STATE          = configuraciones.TITLE_STATE
HABILITAR_ICON_PAGES = configuraciones.HABILITAR_ICON_PAGES
ACT_STATE_0          = configuraciones.ACT_STATE_0
ACT_STATE_1          = configuraciones.ACT_STATE_1
NOMBRE_CRUD_PAGE     = configuraciones.NOMBRE_CRUD_PAGE
NOMBRE_ADMINPAGES_PAGE = configuraciones.NOMBRE_ADMINPAGES_PAGE 
NOMBRE_OPTIONS_COL   = configuraciones.NOMBRE_OPTIONS_COL
NOMBRE_BTN_INSERT    = configuraciones.NOMBRE_BTN_INSERT
NOMBRE_BTN_UPDATE    = configuraciones.NOMBRE_BTN_UPDATE
NOMBRE_BTN_DELETE    = configuraciones.NOMBRE_BTN_DELETE
NOMBRE_BTN_UNACTIVE  = configuraciones.NOMBRE_BTN_UNACTIVE
NOMBRE_BTN_LIST      = configuraciones.NOMBRE_BTN_LIST
NOMBRE_BTN_CONSULT   = configuraciones.NOMBRE_BTN_CONSULT
NOMBRE_BTN_SEARCH    = configuraciones.NOMBRE_BTN_SEARCH
ICON_PAGE_NOICON     = configuraciones.ICON_PAGE_NOICON 
ICON_PAGE_CRUD       = configuraciones.ICON_PAGE_CRUD 
ICON_PAGE_REPORT     = configuraciones.ICON_PAGE_REPORT 
ICON_PAGE_DASHBOARD  = configuraciones.ICON_PAGE_DASHBOARD 
ICON_PAGE_PANEL      = configuraciones.ICON_PAGE_PANEL 
ICON_LIST            = configuraciones.ICON_LIST
ICON_CONSULT         = configuraciones.ICON_CONSULT
ICON_SEARCH          = configuraciones.ICON_SEARCH
ICON_INSERT          = configuraciones.ICON_INSERT
ICON_UPDATE          = configuraciones.ICON_UPDATE
ICON_DELETE          = configuraciones.ICON_DELETE
ICON_ACTIVE          = configuraciones.ICON_ACTIVE
ICON_UNACTIVE        = configuraciones.ICON_UNACTIVE
ICON_UNLOCK          = configuraciones.ICON_UNLOCK


@app.route("/")
def index():
    return render_template("index.html")  # Si tienes un index.html con interfaz

@app.route("/categorias")
def categorias():
    return jsonify(controlador_categoria.obtener_categorias())

@app.route("/preguntas_por_categoria/<int:cat_id>")
def preguntas_por_categoria(cat_id):
    return jsonify(controlador_pregunta.obtener_preguntas_por_categoria(cat_id))

@app.route("/preguntar_json", methods=["POST"])
def preguntar_json():
    data = request.get_json()
    pregunta = data.get("pregunta", "")
    respuesta = controlador_pregunta.buscar_respuesta_por_palabra(pregunta)
    if not respuesta:
        respuesta = "No encontré una respuesta precisa. ¿Puedes reformular tu pregunta?"
    return jsonify({"respuesta": respuesta})

@app.route("/index_2")
def index_2():
    return render_template("index_2.html")  # Si tienes un index.html con interfaz

@app.route("/respuesta_directa", methods=["POST"])
def respuesta_directa():
    data = request.get_json()
    titulo = data.get("titulo", "")
    
    from controladores.controlador_pregunta import obtener_respuesta_por_titulo
    respuesta = obtener_respuesta_por_titulo(titulo)
    
    return jsonify({"respuesta": respuesta or "No encontré esa pregunta."})

@app.route("/preguntar_con_pln", methods=["POST"])
def preguntar_con_pln():
    data = request.get_json()
    pregunta = data.get("pregunta", "")
    respuesta = controlador_pregunta.buscar_respuesta_por_palabra(pregunta)
    if not respuesta:
        respuesta = modelo_semantico.buscar_pregunta_similar(pregunta)
    if not respuesta:
        respuesta = "No encontré una respuesta. ¿Podrías reformular la pregunta?"

    return jsonify({"respuesta": respuesta})


############################################################################################################################
#Opciones para activar o desacticar
def get_options_active():
    lista = [
        [ 0 , STATE_0 ],
        [ 1 , STATE_1 ],
    ]
    return lista

#Opciones de paginación 
def get_options_pagination_crud():
    lista = [ 5 , 10 , 15 , 20 , 25  ]
    selected_option_crud = 20
    return lista , selected_option_crud

#Obtiene el ícono, si no hay, retorna uno por defecto
def get_icon_page(icon):
    if not icon or icon == '':
        return ICON_PAGE_CRUD 
    else:
        return icon 


# Convertir lista en tabla de 2 columnas
def extract_col_row(lista):
    columns = []
    rows = []

    for c , r in lista:
        columns.append( c )
        rows.append( r )

    return [columns , rows]

###########################################CONTROLADORES#################################################



CONTROLADORES = {
    "categoria": {
        "active" : True ,
        "titulo": "categoría de preguntas",
        "nombre_tabla": "categoria",
        "controlador": controlador_categoria,
        "icon_page": 'fa-solid fa-id-card',
        "filters": [
            ['activo', f'{TITLE_STATE}', get_options_active() ],
        ] ,
        "fields_form": [
#            ID/NAME       LABEL              PLACEHOLDER    TYPE        REQUIRED   ABLE/DISABLE   DATOS
            ['id',          'ID',              'ID',          'text',     True ,     False ,        None ],
            ['nombre',      'Nombre',          'Nombre',      'text',     True ,     True  ,        None ],
            ['activo',      f'{TITLE_STATE}',  'Activo',      'p',        True ,     False ,        None ],
        ],
        "crud_forms": {
            "crud_list": True ,
            "crud_search": True ,
            "crud_consult": True ,
            "crud_insert": True ,
            "crud_update": True ,
            "crud_delete": True ,
            "crud_unactive": True ,
        }
    },
}




# @app.route("/preguntar", methods=["POST"])
# def preguntar():
#     pregunta_usuario = request.form.get("pregunta")
#     respuesta = buscar_respuesta_por_palabra(pregunta_usuario)
#     if not respuesta:
#         respuesta = "Lo siento, no encontré una respuesta para tu pregunta."

#     return render_template("index_2.html", respuesta=respuesta)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
