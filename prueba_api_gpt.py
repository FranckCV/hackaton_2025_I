
import openai
from api_bd import sql_select_fetchall

# Configura tu API key de OpenAI aquí
openai.api_key = GPT_API_KEY


# Buscar preguntas relacionadas (vía API)
def buscar_preguntas_similares(texto, limite=3):
    sql = """
        SELECT DISTINCT p.titulo, p.respuesta
        FROM pregunta p
        LEFT JOIN palabra_clave pk ON pk.PREGUNTAid = p.id
        WHERE LOWER(p.titulo) LIKE %s
           OR LOWER(p.respuesta) LIKE %s
           OR LOWER(pk.palabra) LIKE %s
        LIMIT %s
    """
    like = f"%{texto.lower()}%"
    return sql_select_fetchall(sql, [like, like, like, limite])


# Crear prompt para enviar a OpenAI
def construir_prompt(user_input, ejemplos):
    prompt = f"El usuario ha preguntado: \"{user_input}\"\n\nBase de datos de respuestas:\n"
    for i, ej in enumerate(ejemplos, 1):
        prompt += f"{i}. {ej['titulo']} → {ej['respuesta']}\n"
    prompt += "\nResponde de forma clara y amable usando esta información:"
    return prompt


# Enviar prompt a ChatGPT
def responder_con_gpt(prompt):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "Eres un asistente de orientación académica que responde con claridad, brevedad y educación."
            )},
            {"role": "user", "content": prompt}
        ]
    )
    return res['choices'][0]['message']['content']


# Chat en consola
def iniciar_chatbot():
    print("🤖 Chatbot Académico (escribe 'salir' para terminar)\n")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == "salir":
            print("Bot: ¡Hasta luego! 👋")
            break

        similares = buscar_preguntas_similares(pregunta)
        # print(similares)
        if similares:
            prompt = construir_prompt(pregunta, similares)
            respuesta = responder_con_gpt(prompt)
            print("Bot:", respuesta)
        else:
            print("Bot: No encontré información parecida. ¿Puedes intentar con otra formulación?")


# Ejecutar
if __name__ == "__main__":
    iniciar_chatbot()
