import main_controlador
from datetime import datetime

def simulador_chat_gpt():
    print("=== Simulador de Chatbot GPT ===")
    print("Escribe 'salir' para terminar la simulación.\n")

    while True:
        texto_usuario = input("👤 Tú: ").strip()
        if texto_usuario.lower() == "salir":
            print("👋 Cerrando simulación...")
            break

        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            respuesta, docs = main_controlador.responder_gpt_con_doc_soporte(texto_usuario, fecha_actual)
            
            print(f"\n🤖 GPT: {respuesta}\n")

            if docs:
                print("📎 Documentos sugeridos:")
                for doc in docs:
                    print(f"- {doc['titulo']}: {doc['url']}")

            print("\n" + "-"*50 + "\n")

        except Exception as e:
            print(f"⚠️ Error durante la simulación: {e}")
            break

if __name__ == "__main__":
    simulador_chat_gpt()
