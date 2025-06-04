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

# @app.route("/preguntar", methods=["POST"])
# def preguntar():
#     pregunta_usuario = request.form.get("pregunta")
#     respuesta = buscar_respuesta_por_palabra(pregunta_usuario)
#     if not respuesta:
#         respuesta = "Lo siento, no encontré una respuesta para tu pregunta."

#     return render_template("index_2.html", respuesta=respuesta)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
