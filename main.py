from flask import Flask, render_template, request
from controladores.controlador_pregunta import buscar_respuesta_por_palabra
import os
import requests
from dotenv import load_dotenv

from flask import jsonify, make_response, redirect, url_for, flash, session  # si los necesitas
from datetime import datetime, date
import hashlib
import base64

load_dotenv()

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")  # Si tienes un index.html con interfaz

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
