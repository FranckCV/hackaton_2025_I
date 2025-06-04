import os
import openai
from dotenv import load_dotenv
from controladores import controlador_pregunta

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("ERROR: OPENAI_API_KEY no definido en .env")

# === Obtener conocimiento desde base de datos ===
def obtener_conocimiento_usat():
    conexion = controlador_pregunta.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT titulo, respuesta FROM PREGUNTA")
        datos = cursor.fetchall()
    conexion.close()
    return datos

def construir_contexto_con_bd():
    datos = obtener_conocimiento_usat()
    partes = [f"{d['titulo']}: {d['respuesta']}" for d in datos]
    return "\n".join(partes)[:3500]

def preguntar_a_gpt(contexto, texto_usuario):
    messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente académico oficial de la Universidad Católica Santo Toribio de Mogrovejo (USAT), ubicada en Chiclayo, Perú. "
                "Responde únicamente preguntas institucionales o administrativas relacionadas con la USAT. "
                "Esto incluye temas como carreras, admisión, matrícula, horarios, sedes, facultades, docentes, servicios estudiantiles, vida universitaria y cualquier otra consulta directamente vinculada a la universidad.\n\n"

                "Si la pregunta del usuario NO menciona explícitamente a la USAT o a sus servicios, facultades, carreras o sedes, "
                "asume que no está relacionada. En esos casos, responde únicamente con:\n"
                "\"Este chat solo responde consultas académicas relacionadas con la USAT.\"\n\n"

                "Si la pregunta es válida, responde en español de forma amable, clara y profesional. "
                "Puedes usar listas, párrafos bien redactados, títulos llamativos y emojis si ayudan a la claridad.\n\n"

                "A continuación tienes información institucional útil extraída desde una base de datos:\n\n"
                f"{contexto}\n\n"

                "Si no tienes información suficiente para responder con certeza, puedes sugerir al usuario consultar el sitio web oficial: https://www.usat.edu.pe"
            )
        },
        {"role": "user", "content": texto_usuario}
    ]

    respuesta = openai.chat.completions.create(
        model="gpt-4o",  # Puedes usar "gpt-4" o "gpt-3.5-turbo" si no tienes acceso
        messages=messages,
        max_tokens=600,
        temperature=0.5
    )

    return respuesta.choices[0].message.content.strip()


def responder(texto_usuario):
    contexto_bd = construir_contexto_con_bd()
    return preguntar_a_gpt(contexto_bd, texto_usuario)

if __name__ == "__main__":
    print("=== Chatbot USAT 🤖 ===")
    while True:
        entrada = input("\nTú: ").strip()
        if entrada.lower() in ("salir", "exit", "quit"):
            print("👋 ¡Hasta pronto!")
            break
        print("🤖 Pensando...")
        respuesta = responder(entrada)
        print(f"Bot: {respuesta}")


# {
#             "role": "system",
#             "content": (
#                 "Eres un asistente académico experto en la Universidad Católica Santo Toribio de Mogrovejo (USAT), en Perú. "
#                 "Responde siempre en español, de manera clara, amigable y profesional. "
#                 "Puedes usar tu conocimiento general junto con el siguiente contexto (extraído de la base de datos):\n\n"
#                 f"{contexto}\n\n"
#                 "Si no estás seguro de algo, responde educadamente o sugiere visitar el sitio oficial: https://www.usat.edu.pe"
#             )
#         }