import configuraciones
URL_NGROK = configuraciones.URL_SITE
VERIFY_TOKEN = configuraciones.VERIFY_TOKEN

from flask import Flask, request ,jsonify
import requests
from datetime import datetime
import pytz

from function_wsp import send_wsp_document, send_wsp_msg , send_wsp_list_options

app = Flask(__name__)


def local_hour():
    return datetime.now(pytz.utc).astimezone(pytz.timezone('America/Lima')).isoformat()


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Token inválido", 403

    elif request.method == "POST":
        try:
            data = request.get_json()
            message = data["entry"][0]["changes"][0]["value"]["messages"][0]
            sender = message["from"]
            
            
            ############código agregado
            # REGISTRAR USUARIO SI NO EXISTE
            requests.post(f"{URL_NGROK}insert_usuario_chat", json={
                "numero": sender
            }, timeout=5)
            ######################
            
            tipo = message["type"]
            fecha = local_hour()

            # Insertar webhook en BD a través de API en ngrok
            requests.post(f"{URL_NGROK}insert_webhook", json={
                "data": data,
                "fecha": str(fecha)
            }, timeout=10)

            # Procesar mensaje en ngrok
            payload_data = {
                "sender": sender,
                "tipo": tipo,
                "fecha": str(fecha),
                "message": message
            }
            res = requests.post(f"{URL_NGROK}procesar_mensaje", json=payload_data, timeout=30)

            if res.ok:
                data_res = res.json()
                respuesta = data_res.get("respuesta", "Lo siento, no pude procesar tu solicitud.")
                documentos = data_res.get("documentos", [])
                tipo_envio = data_res.get("tipo_envio", "texto")

                if tipo_envio == "lista":
                    rows = data_res.get("lista_opciones", [])
                    section_title = data_res.get("section_title", "Opciones disponibles")
                    response1 = send_wsp_list_options(sender, respuesta, rows, section_title)
                else:
                    response1 = send_wsp_msg(sender, respuesta)

                # Enviar documentos si existen
                for doc in documentos:
                    response2 = send_wsp_document(sender, doc["url"], doc["titulo"])

                return f"OK , msg: {message} , rpta: {respuesta} , response: {response1.text}", 200

            else:
                send_wsp_msg(sender, "Lo siento, ocurrió un error al procesar tu solicitud.")
                return f"ERROR {res.status_code} {res.text}", 200

        except Exception as e:
            return f"ERROR EN WEBHOOK: {e}", 200


@app.route("/insert_usuario_chat", methods=["POST"])
def insert_usuario_chat():
    try:
        data = request.get_json()
        numero = data.get("numero")

        if not numero:
            return jsonify({"error": "Número no proporcionado"}), 400

        from controladores import bd
        sql_check = "SELECT 1 FROM usuarios_chat WHERE numero = %s"
        existe = bd.sql_select_fetchone(sql_check, (numero,))

        if not existe:
            sql_insert = "INSERT INTO usuarios_chat (numero) VALUES (%s)"
            bd.sql_execute(sql_insert, (numero,))
        
        return jsonify({"message": "Usuario registrado"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
