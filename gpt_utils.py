import openai
import controladores.bd as bd
import configuraciones

openai.api_key = configuraciones.API_GPT

def ejecutar_prompt( content , prompt ):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                content
            )},
            {"role": "user", "content": prompt}
        ]
    )
    # print(respuesta)
    return respuesta['choices'][0]['message']['content']



def verificar_si_gpt_respondio(pregunta_usuario, respuesta_generada):
    prompt = (
        f"Pregunta del usuario: \"{pregunta_usuario}\"\n\n"
        f"Respuesta generada por el asistente: \"{respuesta_generada}\"\n\n"
        "¿La respuesta fue útil y responde la pregunta claramente con información institucional de la USAT?\n\n"
        "Responde solo con un número:\n"
        "1 → Sí responde correctamente\n"
        "0 → No responde o es ambigua/inútil\n"
    )

    content = (
        "Eres un verificador que evalúa si la respuesta entregada al usuario realmente responde la consulta. "
        "No des explicaciones, solo responde con 1 o 0. "
        "Si la respuesta fue genérica, ambigua o no útil, responde 0. "
        "Si sí responde claramente con base en información institucional, responde 1."
    )

    resultado = ejecutar_prompt(content, prompt).strip()

    # Aseguramos que devuelva 0 o 1 como entero
    if "1" in resultado:
        return 1
    return 0


def ejecutar_prompt_usat( prompt ):
    content = (
        "Eres un asistente académico oficial de la escuela de Ingenieria en Sistemas y Computación de la Universidad Católica Santo Toribio de Mogrovejo (USAT), ubicada en Chiclayo, Perú. "
        "Interpreta los mensajes para que respondas únicamente preguntas institucionales o administrativas relacionadas con la informacion entregada de USAT."
        "Si despues de interpretar la pregunta, esta no tiene ninguna relación con USAT, responde: \"Este chat solo responde consultas académicas relacionadas con la USAT.\""
        "Después de responder correctamente, sugierele al usuario que si tiene más dudas siga escribiendo, o si ya terminó que escriba \"Salir\" para finalizar la conversación"
        "Redacta esta respuesta de forma amable, clara y profesional, como si fueras un asistente académico de la USAT, hablando con naturalidad. Puedes usar emojis si mejora la comprensión." \
        "Si el usuario te pide directamente documentos o archivos que tu puedes sugerirle porque están en la base de datos, se los envias"
        "Puedes consultar informacion de internet pero solo de las páginas más recientes de USAT . No inventes datos. No es necesario que saludes más de una vez. "
    )
    respuesta = ejecutar_prompt( content , prompt )

    return respuesta



def responder_con_gpt_modo_abierto(user_input, ejemplos , fecha ):
    prompt = f"El usuario ha preguntado: \"{user_input}\"\n\nBase de datos de respuestas:\n"
    for i, ej in enumerate(ejemplos, 1):
        prompt += f"{i}. {ej['titulo']} → {ej['respuesta']}\n"
    # prompt += "\nResponde de forma clara, amable y natural usando esta información."
    respuesta = ejecutar_prompt_usat( prompt )

    fue_util = verificar_si_gpt_respondio(user_input, respuesta)

    if str(fue_util) == str('0'):
        bd.insert_data_historial( user_input, fecha  )
    return respuesta




