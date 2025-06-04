




# NO SE GUIEN DE ESTO TONOTOS



































import requests
from flask import Flask, request , json , jsonify
import api_bd 

def get_webhook():
    sql ='''
        select * from webhook order by fecha desc
    '''
    filas = api_bd.sql_select_fetchall(sql)
    return filas

def get_respuesta_pregunta(pregunta):
    sql ='''
        select
            titulo ,
            respuesta
        from
        PREGUNTA
        where UPPER(titulo) LIKE UPPER(%s)
    '''
    res = api_bd.sql_select_fetchone(sql, (pregunta))
    return res


def get_api_msg():
    return requests.get("https://franckcv.pythonanywhere.com/api/mensajes")


def get_response_api(url):
    return requests.get(url)

def force_json(data):
    return json.loads(data)

app = Flask(__name__)

def extract_msg_data(msg):
    fecha = msg.get('fecha')
    dato = force_json(msg.get('dato'))
    if dato:
        entry = dato.get('entry')
        if entry:
            changes = entry[0].get('changes')
            if changes:
                value = changes[0].get('value')
                if value:
                    contacts = value.get('contacts')
                    messages = value.get('messages')
                    if contacts and messages:
                        name = contacts[0].get('profile').get('name')
                        from_t = messages[0].get('from')
                        body = messages[0].get('text').get('body')
                        lista = [fecha , from_t , name , body ]
                        return lista


@app.route("/lista")
def lista():
    data = get_webhook()
    lista = []
    for msg in data:
        info = extract_msg_data(msg)
        # print(info)
        lista.append(info)

    # aaa = { 
    #         "entry": [
    #             {
    #                 "changes": [
    #                     {
    #                         "field": "messages",
    #                         "value": {
    #                             "contacts": [
    #                                 {
    #                                     "profile": {
    #                                         "name": "Junior"
    #                                     },
    #                                     "wa_id": "51948938578"
    #                                 }
    #                             ],
    #                             "messages": [
    #                                 {
    #                                 "from": "51948938578",
    #                                 "id": "wamid.HBgLNTE5NDg5Mzg1NzgVAgASGBYzRUIwQkNGRDMxQzgyQTA5NTE4ODBCAA==",
    #                                 "text": {
    #                                     "body": "buaaaaaaaaaa"
    #                                 },
    #                                 "timestamp": "1749015647",
    #                                 "type": "text"
    #                                 }
    #                             ],
    #                             "messaging_product": "whatsapp",
    #                             "metadata": {
    #                                 "display_phone_number": "15551632231",
    #                                 "phone_number_id": "601214496418181"
    #                             }
    #                         }
    #                     }
    #                 ],
    #                 "id": "4190426744616386"
    #             }
    #         ],
    #         "object": "whatsapp_business_account"
    #     }

    # data = transform_text_to_json(text)

    # return jsonify(lista)
    return f'LISTA: {lista}'


@app.route("/")
def datos():
    data = get_webhook()
    # print(controlador.get_respuesta_pregunta('Idioma inglés'))
    texto = ''
    for msg in data:
        info = extract_msg_data(msg)
        texto += f'''<p>{info}</p>'''

    return f'{texto}'






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)




