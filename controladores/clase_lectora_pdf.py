import fitz  # PyMuPDF
from docx import Document
import pandas as pd
import os
from werkzeug.utils import secure_filename

class LectorArchivo:
    def __init__(self, carpeta_destino="../static/docs"):
        self.upload_folder = os.path.abspath(carpeta_destino)
        self.extensiones_permitidas = {'pdf', 'docx', 'xlsx', 'csv'}

        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.extensiones_permitidas

    def guardar_archivo(self, archivo):
        if archivo and self.allowed_file(archivo.filename):
            filename = secure_filename(archivo.filename)
            ruta_completa = os.path.join(self.upload_folder, filename)
            archivo.save(ruta_completa)
            return filename, ruta_completa
        return None, None

    def leer_pdf(self, ruta, max_chars=2000):
        try:
            texto = ""
            with fitz.open(ruta) as doc:
                for page in doc:
                    texto += page.get_text()
                    if len(texto) >= max_chars:
                        break
            return texto.strip().replace('\n', ' ')
        except Exception as e:
            return f"[ERROR PDF] {e}"

    def leer_docx(self, ruta):
        try:
            documento = Document(ruta)
            return "\n".join([p.text for p in documento.paragraphs])
        except Exception as e:
            return f"[ERROR DOCX] {e}"

    def leer_xlsx(self, ruta):
        try:
            df = pd.read_excel(ruta)
            return df.to_string(index=False)
        except Exception as e:
            return f"[ERROR XLSX] {e}"

    def leer_csv(self, ruta):
        try:
            df = pd.read_csv(ruta)
            return df.to_string(index=False)
        except Exception as e:
            return f"[ERROR CSV] {e}"

    def leer(self, ruta):
        extension = os.path.splitext(ruta)[-1].lower()
        if extension == ".pdf":
            return self.leer_pdf(ruta)
        elif extension == ".docx":
            return self.leer_docx(ruta)
        elif extension == ".xlsx":
            return self.leer_xlsx(ruta)
        elif extension == ".csv":
            return self.leer_csv(ruta)
        else:
            return "[ERROR] Formato no soportado"
