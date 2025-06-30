import configuraciones
import requests

ACCESS_TOKEN = configuraciones.ACCESS_TOKEN
WSP_URL = configuraciones.WSP_URL

def send_wsp_document(recipient_number, file_url, filename="documento.pdf"):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "document",
        "document": {
            "link": file_url,
            "filename": filename
        }
    }

    return requests.post(WSP_URL, headers=headers, json=data)



def send_wsp_list_options(recipient_number, text, options, section_title="Opciones"):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": text
            },
            "action": {
                "button": "Ver opciones",
                "sections": [
                    {
                        "title": section_title,
                        "rows": options
                    }
                ]
            }
        }
    }

    response = requests.post(WSP_URL, headers=headers, json=data)
    return response


def send_wsp_options( recipient_number , text , buttons):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": text
            },
            "action": {
                "buttons": buttons
            }
        }
    }
    response = requests.post(WSP_URL, headers=headers, json=data)
    return response


def send_wsp_msg( recipient_number , text ):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "text",
        "text": {
            "body": text
        }
    }
    response = requests.post(WSP_URL, headers=headers, json=data)
    return response


