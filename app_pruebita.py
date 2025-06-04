# import requests
# import json

# # Configuración
# API_KEY = "TU_API_KEY_AQUI"
# PHONE_NUMBER_ID = "TU_PHONE_NUMBER_ID"
# RECIPIENT_PHONE_NUMBER = "51987654321"  # Número del usuario, con código de país
# MENSAJE = "Hola, este es un mensaje de prueba desde mi bot 😎"

# # URL de la API de WhatsApp de 360dialog
# url = f"https://waba.360dialog.io/v1/messages"

# # Cabeceras de autenticación
# headers = {
#     "D360-API-KEY": API_KEY,
#     "Content-Type": "application/json"
# }

# # Cuerpo del mensaje
# data = {
#     "recipient_type": "individual",
#     "to": RECIPIENT_PHONE_NUMBER,
#     "type": "text",
#     "text": {
#         "body": MENSAJE
#     }
# }

# # Enviar mensaje
# response = requests.post(url, headers=headers, data=json.dumps(data))

# # Mostrar resultado
# print("Código de estado:", response.status_code)
# print("Respuesta:", response.json())
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("ERROR: OPENAI_API_KEY no está definida.")

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("pruebita.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    texto_usuario = data.get("mensaje", "").strip()
    if texto_usuario == "":
        return jsonify({"error": "El campo 'mensaje' no puede estar vacío."}), 400

    try:
        # ↓ aquí usamos la llamada migra da a la nueva interfaz (openai>=1.0.0):
        respuesta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente muy servicial que responde en español."},
                {"role": "user",   "content": texto_usuario}
            ],
            max_tokens=200,
            temperature=0.7
        )
        contenido = respuesta.choices[0].message.content.strip()
        return jsonify({"respuesta": contenido})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
