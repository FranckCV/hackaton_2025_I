from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "midetoken123"  # Puedes poner el que tú quieras

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verificación del webhook
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Token inválido", 403

    elif request.method == "POST":
        data = request.get_json()
        print("📩 Mensaje recibido:", data)
        return "EVENT_RECEIVED", 200


app.run(port=5000)
