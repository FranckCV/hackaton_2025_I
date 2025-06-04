import requests

ACCESS_TOKEN = 'EAAUc4yYrWtcccBOZCYHFNO87bqIK0WStOmcjL7v7ag7EpUfLfzFzkHDMWpnVUNOkNUor6p5BZCRRQ4NUdtX2TJsJo3mU0g0B9YduFZBqNUxtXC3ixe9qfZBbXKHOZARjtLvG1Lz718312oV1ZBpz1wZCStAp4G7ZAiSFzqOrJf3OAUO5BQdC2gDpSRaS48nH8fi69Q0VhYjAGt7ZAzyvDsrZC1UjnqRSFEPBWS1PITVP'
PHONE_NUMBER_ID = '601214496418181'  # Lo encuentras en developers.facebook.com > WhatsApp > configuración
# RECIPIENT_PHONE_NUMBER = '51948938578'  # Con código de país, sin signos ni espacios
RECIPIENT_PHONE_NUMBER = '51966302879'  # Con código de país, sin signos ni espacios

url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "messaging_product": "whatsapp",
    "to": RECIPIENT_PHONE_NUMBER,
    "type": "text",
    "text": {
        "body": "Hola tonoto jiji"
    }
}

response = requests.post(url, headers=headers, json=data)
print("Código:", response.status_code)
print("Respuesta:", response.json())