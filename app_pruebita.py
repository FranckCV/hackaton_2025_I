import os
from flask import Flask, request, jsonify
import controladores.controlador_pregunta as controlador_pregunta
import requests
from dotenv import load_dotenv
import openai

load_dotenv()
app = Flask(__name__)


ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
if not ACCESS_TOKEN:
    raise RuntimeError("ERROR: WhatsApp ACCESS_TOKEN no definido en .env")


openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("ERROR: OPENAI_API_KEY no definido en .env")


VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN") 

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Validación inicial de Facebook/Meta
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        return "Error de validación", 403

    # Si es POST, es un mensaje entrante
    payload = request.get_json()
    # 4.1) Extraer el phone_number_id para poder responder
    try:
        entry = payload["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]
        metadata = value["metadata"]
        PHONE_NUMBER_ID = metadata["phone_number_id"] 
    except Exception as e:
        print("[ERROR] No pude extraer phone_number_id:", e)
        return "Ok", 200  

    # 4.2) Extraer número remitente y texto
    try:
        contacto = value["contacts"][0]
        remitente = contacto["wa_id"] 
        mensaje = value["messages"][0]
        if mensaje.get("type") != "text":
            return "Solo texto soportado", 200
        texto_usuario = mensaje["text"]["body"].strip()
    except Exception as e:
        print("[ERROR] No pude extraer remitente/texto:", e)
        return "Ok", 200

    # 4.3) Intentar obtener respuesta directa desde la BD
    texto_bd = controlador_pregunta.buscar_respuesta_por_palabra(texto_usuario)
    if texto_bd:
        texto_gpt = texto_bd
    else:
        # 4.4) Si no hay coincidencia en la BD, llamar a OpenAI
        system_message = {
            "role": "system",
            "content": (
                "Eres un chatbot oficial de la USAT. "
                "Responde únicamente sobre carreras, admisión, costos, fechas, sedes y servicios de la universidad católica santo toribio de Mogrovejo en chiclayo, Lambayeque, Perú. "
                "Si la pregunta NO está relacionada con la  universidad católica santo toribio de Mogrovejo en chiclayo, Lambayeque, Perú, responde exactamente: "
                "\"Este chat solo admite preguntas académicas sobre la USAT.\" "
                "Si la pregunta está relacionada, mantén tu respuesta breve y en español."
            )
        }
        user_message = {"role": "user", "content": texto_usuario}

        try:
            respuesta_ai = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[system_message, user_message],
                max_tokens=250,
                temperature=0.5
            )
            texto_gpt = respuesta_ai.choices[0].message.content.strip()
        except Exception as e:
            print("[ERROR OPENAI]", e)
            texto_gpt = "Lo siento, hubo un error procesando tu mensaje."

    # 4.5) Enviar la respuesta (de BD o de GPT) vía Graph API de WhatsApp
    url = f"https://graph.facebook.com/v15.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    cuerpo = {
        "messaging_product": "whatsapp",
        "to": remitente,
        "type": "text",
        "text": {"body": texto_gpt}
    }

    try:
        resp = requests.post(url, headers=headers, json=cuerpo)
        if resp.status_code not in (200, 201):
            print("[ERROR WHATSAPP SEND]", resp.status_code, resp.text)
    except Exception as e:
        print("[ERROR REQUEST]", e)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
