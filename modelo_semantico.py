from sentence_transformers import SentenceTransformer, util
from controladores.bd import obtener_conexion

modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def cargar_preguntas_frecuentes():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, titulo, respuesta FROM PREGUNTA")
        preguntas = cursor.fetchall()
    conexion.close()
    return preguntas

preguntas_frecuentes = cargar_preguntas_frecuentes()
titulos = [p['titulo'] for p in preguntas_frecuentes]
embeddings_titulos = modelo.encode(titulos, convert_to_tensor=True)

def buscar_pregunta_similar(texto_usuario, umbral_similitud=0.6):
    embedding_usuario = modelo.encode(texto_usuario, convert_to_tensor=True)
    similitudes = util.pytorch_cos_sim(embedding_usuario, embeddings_titulos)[0]
    indice_mejor = similitudes.argmax().item()
    mejor_score = similitudes[indice_mejor].item()

    if mejor_score >= umbral_similitud:
        return preguntas_frecuentes[indice_mejor]['respuesta']
    else:
        return None
