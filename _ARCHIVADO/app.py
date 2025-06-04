import requests
import json

# Configuración
API_KEY = "TU_API_KEY_AQUI"
PHONE_NUMBER_ID = "TU_PHONE_NUMBER_ID"
RECIPIENT_PHONE_NUMBER = "51987654321"  # Número del usuario, con código de país
MENSAJE = "Hola, este es un mensaje de prueba desde mi bot 😎"

# URL de la API de WhatsApp de 360dialog
url = f"https://waba.360dialog.io/v1/messages"

# Cabeceras de autenticación
headers = {
    "D360-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

# Cuerpo del mensaje
data = {
    "recipient_type": "individual",
    "to": RECIPIENT_PHONE_NUMBER,
    "type": "text",
    "text": {
        "body": MENSAJE
    }
}

# Enviar mensaje
response = requests.post(url, headers=headers, data=json.dumps(data))

# Mostrar resultado
print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
