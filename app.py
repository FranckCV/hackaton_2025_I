from flask import Flask, render_template, request, redirect,  jsonify,  make_response,   url_for, json
import main_controlador
from werkzeug.utils import secure_filename
import configuraciones
import controladores.controlador_usuario as controlador_usuario
import controladores.controlador_pregunta as controlador_pregunta
import controladores.controlador_categoria as controlador_categoria
import controladores.controlador_historial as controlador_historial
import controladores.controlador_palabra_clave as controlador_palabra_clave
import controladores.controlador_pregunta as controlador_pregunta
import controladores.controlador_documento as controlador_documento
import controladores.controlador_dashboard as controlador_dashboard
from controladores import clase_lectora_pdf as clase_lectora_pdf
import controladores.bd as bd
import fitz  # PyMuPDF

import os
import requests
from functools import wraps
import inspect

# import ast
# import _ARCHIVADO.modelo_semantico as modelo_semantico
# from datetime import datetime, date
# load_dotenv()

app = Flask(__name__, template_folder='templates')


VERIFY_TOKEN           = configuraciones.VERIFY_TOKEN
ACCESS_TOKEN           = configuraciones.ACCESS_TOKEN
PHONE_NUMBER_ID        = configuraciones.PHONE_NUMBER_ID
RECIPIENT_PHONE_NUMBER = configuraciones.RECIPIENT_PHONE_NUMBER
WSP_URL                = configuraciones.WSP_URL
URL_SITE               = configuraciones.URL_SITE
PYTHON_URL             = configuraciones.PYTHON_URL

resp = requests.post(
    f"{PYTHON_URL}set_ngrok_url",
    json={"url": URL_SITE},
    timeout=10
)


STATE_0                = configuraciones.STATE_0
STATE_1                = configuraciones.STATE_1
TITLE_STATE            = configuraciones.TITLE_STATE
HABILITAR_ICON_PAGES   = configuraciones.HABILITAR_ICON_PAGES
ACT_STATE_0            = configuraciones.ACT_STATE_0
ACT_STATE_1            = configuraciones.ACT_STATE_1
NOMBRE_CRUD_PAGE       = configuraciones.NOMBRE_CRUD_PAGE
NOMBRE_ADMINPAGES_PAGE = configuraciones.NOMBRE_ADMINPAGES_PAGE
NOMBRE_OPTIONS_COL     = configuraciones.NOMBRE_OPTIONS_COL
NOMBRE_BTN_INSERT      = configuraciones.NOMBRE_BTN_INSERT
NOMBRE_BTN_UPDATE      = configuraciones.NOMBRE_BTN_UPDATE
NOMBRE_BTN_DELETE      = configuraciones.NOMBRE_BTN_DELETE
NOMBRE_BTN_UNACTIVE    = configuraciones.NOMBRE_BTN_UNACTIVE
NOMBRE_BTN_LIST        = configuraciones.NOMBRE_BTN_LIST
NOMBRE_BTN_CONSULT     = configuraciones.NOMBRE_BTN_CONSULT
NOMBRE_BTN_SEARCH      = configuraciones.NOMBRE_BTN_SEARCH
ICON_PAGE_NOICON       = configuraciones.ICON_PAGE_NOICON
ICON_PAGE_CRUD         = configuraciones.ICON_PAGE_CRUD
ICON_PAGE_REPORT       = configuraciones.ICON_PAGE_REPORT
ICON_PAGE_DASHBOARD    = configuraciones.ICON_PAGE_DASHBOARD
ICON_PAGE_PANEL        = configuraciones.ICON_PAGE_PANEL
ICON_LIST              = configuraciones.ICON_LIST
ICON_CONSULT           = configuraciones.ICON_CONSULT
ICON_SEARCH            = configuraciones.ICON_SEARCH
ICON_INSERT            = configuraciones.ICON_INSERT
ICON_UPDATE            = configuraciones.ICON_UPDATE
ICON_DELETE            = configuraciones.ICON_DELETE
ICON_ACTIVE            = configuraciones.ICON_ACTIVE
ICON_UNACTIVE          = configuraciones.ICON_UNACTIVE
ICON_UNLOCK            = configuraciones.ICON_UNLOCK


def force_json(data):
    return json.loads(data)


def truncar_texto(texto, max_len=24):
    return texto if len(texto) <= max_len else texto[:max_len - 3].strip() + "..."


def extract_message_entry(data):
    return force_json(data)["entry"][0]["changes"][0]["value"]["messages"][0]


@app.route("/insert_webhook", methods=["POST"])
def insert_webhook():
    data = request.get_json()
    raw_data = data.get("data")
    fecha = data.get("fecha")
    main_controlador.insert_data_webhook(raw_data, fecha)
    return {"status": "ok"}


@app.route("/procesar_mensaje", methods=["POST"])
def procesar_mensaje():
    data = request.get_json()
    sender = data.get("sender")
    tipo = data.get("tipo")
    fecha = data.get("fecha")
    message = data.get("message")

    try:
        payload = None
        respuesta = ""
        documentos = []
        tipo_envio = "texto"
        lista_opciones = []
        section_title = ""

        # Si el tipo es botón o interactivo
        if tipo == "button":
            payload = message["button"]["payload"]
        elif tipo == "interactive" and message.get("interactive", {}).get("type") == "list_reply":
            payload = message["interactive"]["list_reply"]["id"]

        if payload:
            if payload == "OTROS_CAT":
                main_controlador.set_estado(sender, "modo_abierto")
                respuesta = "Puedes escribir tu pregunta libremente."
            elif payload.startswith("CAT_"):
                categoria_id = int(payload.split("_")[1])
                main_controlador.set_estado(sender, "preguntas", categoria_id)
                preguntas = main_controlador.get_preguntas_por_categoria(categoria_id)
                rows = [{"id": f"PRE_{p['id']}", "title": p["titulo"], "description": p["titulo"]} for p in preguntas]
                rows.append({"id": "OTROS_PREG", "title": "Otros"})
                respuesta = "Selecciona una pregunta:"
                tipo_envio = "lista"
                lista_opciones = rows
                section_title = "Preguntas disponibles"
            elif payload.startswith("PRE_"):
                pregunta_id = int(payload.split("_")[1])
                respuesta = main_controlador.responder_gpt_desde_pregunta(pregunta_id)
                main_controlador.set_estado(sender, "modo_abierto")
            elif payload == "OTROS_PREG":
                main_controlador.set_estado(sender, "modo_abierto")
                respuesta = "Escribe tu pregunta libremente."

        elif tipo == "text":
            texto = message["text"]["body"].strip()
            if texto.lower() == "salir":
                main_controlador.limpiar_estado(sender)
                respuesta = "¡Gracias por usar el chatbot! Hasta pronto ✌"
            else:
                estado = main_controlador.get_estado(sender)
                if estado == "inicio" or estado is None:
                    main_controlador.set_estado(sender, "categorias")
                    categorias = main_controlador.get_categorias()
                    rows = [{"id": f"CAT_{c['id']}", "title": c["nombre"]} for c in categorias]
                    rows.append({"id": "OTROS_CAT", "title": "Otros"})
                    respuesta = "¡Hola! ¿Sobre qué tema deseas información?"
                    tipo_envio = "lista"
                    lista_opciones = rows
                    section_title = "Categorías disponibles"
                elif estado == "modo_abierto":
                    respuesta, docs = main_controlador.responder_gpt_con_doc_soporte(texto, fecha)
                    if docs:
                        for d in docs:
                            d['url'] = f'{URL_SITE}static/docs/{d.get('url')}' 
                            # print(d)
                            documentos.append(d)
                        # print(documentos)
                    main_controlador.set_estado(sender, "modo_abierto")
                elif estado == "preguntas":
                    categoria_id = main_controlador.get_categoria_actual(sender)
                    respuesta = main_controlador.buscar_pregunta_en_categoria(texto, categoria_id)
                    main_controlador.set_estado(sender, "modo_abierto")

        main_controlador.limpiar_estados_expirados()
        # print(respuesta)
        return jsonify({
            "respuesta": respuesta,
            "documentos": documentos,
            "tipo_envio": tipo_envio,
            "lista_opciones": lista_opciones,
            "section_title": section_title
        })

    except Exception as e:
        return jsonify({"respuesta": f"Error procesando: {e}", "documentos": [], "tipo_envio": "texto"})


@app.route("/get_webhook")
def get_webhook():
    data = bd.sql_select_fetchall('select * from webhook order by fecha desc')
    texto = ''
    for msg in data:
        if msg['dato'] :
            m = force_json(msg['dato'])["entry"][0]["changes"][0]["value"]["messages"][0]
            texto += f'''<p>{m}</p>'''

    return f'{texto}'


@app.route("/")
def index():
    historial = controlador_historial.get_data()
    cantidad_usuarios = controlador_usuario.get_user_count()
    cantidad_historial = controlador_historial.get_question_count()
    return render_template("index.html",historial=historial, cantidad_usuarios = cantidad_usuarios, cantidad_historial = cantidad_historial)  # Si tienes un index.html con interfaz


@app.route("/categorias")
def categorias():
    return jsonify(controlador_categoria.obtener_categorias())


@app.route("/preguntas_por_categoria/<int:cat_id>")
def preguntas_por_categoria(cat_id):
    return jsonify(controlador_pregunta.obtener_preguntas_por_categoria(cat_id))


@app.route("/preguntar_json", methods=["POST"])
def preguntar_json():
    data = request.get_json()
    pregunta = data.get("pregunta", "")
    respuesta = controlador_pregunta.buscar_respuesta_por_palabra(pregunta)
    if not respuesta:
        respuesta = "No encontré una respuesta precisa. ¿Puedes reformular tu pregunta?"
    return jsonify({"respuesta": respuesta})


@app.route("/index_2")
def index_2():
    return render_template("index_2.html")  # Si tienes un index.html con interfaz


@app.route("/respuesta_directa", methods=["POST"])
def respuesta_directa():
    data = request.get_json()
    titulo = data.get("titulo", "")

    from controladores.controlador_pregunta import obtener_respuesta_por_titulo
    respuesta = obtener_respuesta_por_titulo(titulo)

    return jsonify({"respuesta": respuesta or "No encontré esa pregunta."})


@app.route("/panel")
def panel_administrativo():
    modulos = [
        {
            "id": 1,
            "key": "categoria",
            "nombre": "Categorías",
            "icono": "fas fa-list",
            "color": "#2980b9",
        },
        {
            "id": 2,
            "key": "pregunta",
            "nombre": "Preguntas",
            "icono": "fas fa-question-circle",
            "color": "#27ae60",
        },
        {
            "id": 3,
            "key": "historial",
            "nombre": "Historial",
            "icono": "fas fa-history",
            "color": "#f39c12",
        },
        {
            "id": 3,
            "key": "palabra_clave",
            "nombre": "Palabra clave",
            "icono": "fas fa-key",
            "color": "#137372",
        }
    ]
    return render_template("dashboard.html", modulos=modulos)


def get_options_active():
    lista = [
        [ 0 , STATE_0 ],
        [ 1 , STATE_1 ],
    ]
    return lista

#Opciones de paginación
def get_options_pagination_crud():
    lista = [ 5 , 10 , 15 , 20 , 25  ]
    selected_option_crud = 20
    return lista , selected_option_crud

#Obtiene el ícono, si no hay, retorna uno por defecto
def get_icon_page(icon):
    if not icon or icon == '':
        return ICON_PAGE_CRUD
    else:
        return icon


# Convertir lista en tabla de 2 columnas
def extract_col_row(lista):
    columns = []
    rows = []

    for c , r in lista:
        columns.append( c )
        rows.append( r )

    return [columns , rows]

###########################################CONTROLADORES#################################################
ERRORES = {
    "'NoneType' object is not subscriptable" : "Inicie sesión con su cuenta correspondiente",
    "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again." : "El enlace al que intentó ingresar no existe." ,
    "NO_EXISTE_USERNAME" : "El nombre de usuario ingresado ya fue tomado por otro usuario" ,
    "NO_EXISTE_EMAIL" : "El correo electronico ingresado ya fue tomado por otro usuario" ,
    "LOGIN_INVALIDO" : 'Credenciales inválidas. Intente de nuevo' ,
    "foreign key constraint fails" : 'No es posible eliminar dicha fila' ,
}


CONTROLADORES = {
    "categoria": {
        "active" : True ,
        "titulo": "categoría",
        "nombre_tabla": "categoria",
        "controlador": controlador_categoria,
        "icon_page": 'fas fa-tags',
        "filters": [
            ['activo', f'{TITLE_STATE}', get_options_active() ],
        ] ,
        "fields_form": [
#            ID/NAME       LABEL              PLACEHOLDER    TYPE        REQUIRED   ABLE/DISABLE   DATOS
            ['id',          'ID',              'ID',          'text',     True ,     False ,        None ],
            ['nombre',      'Nombre',          'Nombre',      'text',     True ,     True  ,        None ],
            ['activo',      f'{TITLE_STATE}',  'Activo',      'p',        True ,     False ,        None ],
            ['descripcion', 'Descripción',     'descripcion', 'textarea', False,     True  ,        None ],
        ],
        "crud_forms": {
            "crud_list": True ,
            "crud_search": True ,
            "crud_consult": True ,
            "crud_insert": True ,
            "crud_update": True ,
            "crud_delete": True ,
            "crud_unactive": True ,
        }
    },


    "pregunta": {
        "active" : True ,
        "titulo": "Pregunta",
        "nombre_tabla": "pregunta",
        "controlador": controlador_pregunta,
        "icon_page": 'fas fa-question-circle',
        "filters": [
            ['categoriaid', 'Categoría de pregunta', lambda: controlador_categoria.get_options() ],
        ] ,
        "fields_form": [
#            ID/NAME          LABEL               PLACEHOLDER      TYPE         REQUIRED   ABLE/DISABLE   DATOS
            ['id',            'ID',               'ID',            'text',      False ,    False,         True ],
            ['titulo',      'Título',          'Título',      'text',     True ,     True  ,        None ],
            ['categoriaid',  'Nombre de motivo de reclamo', 'Elegir motivo de reclamo', 'select', True ,True, [lambda: controlador_categoria.get_options() , 'nom_cat' ] ],
            ['respuesta', 'Respuesta',     'Respuesta', 'textarea', False,     True  ,        None ],
        ],
        "crud_forms": {
            "crud_list": True ,
            "crud_search": True ,
            "crud_consult": True ,
            "crud_insert": True ,
            "crud_update": True ,
            "crud_delete": True ,
            "crud_unactive": True ,
        }
    },
    "palabra_clave": {
        "active" : True ,
        "titulo": "palabra clave",
        "nombre_tabla": "palabra_clave",
        "controlador": controlador_palabra_clave,
        "icon_page": 'fas fa-key',
        "filters": [
            ['preguntaid', 'Pregunta', lambda: controlador_pregunta.get_options() ],
        ] ,
        "fields_form": [
#            ID/NAME          LABEL               PLACEHOLDER      TYPE         REQUIRED   ABLE/DISABLE   DATOS
            ['id',            'ID',               'ID',            'text',      False ,    False,         True ],
            ['palabra',      'Palabra',          'Palabra',      'text',     True ,     True  ,        None ],
            ['preguntaid',  'Título de pregunta', 'Elegir título de pregunta', 'select', True ,True, [lambda: controlador_pregunta.get_options() , 'titulo_pre' ] ],
        ],
        "crud_forms": {
            "crud_list": True ,
            "crud_search": True ,
            "crud_consult": True ,
            "crud_insert": True ,
            "crud_update": True ,
            "crud_delete": True ,
            "crud_unactive": True ,
        }
    },
     "documento": {
        "active" : True ,
        "titulo": "Documento",
        "nombre_tabla": "documento",
        "controlador": controlador_documento,
        "icon_page": 'fa-solid fa-file',
        "filters": [
            ['preguntaid', 'Seleccione una pregunta', lambda: controlador_pregunta.get_options() ],
                        # ['activo', f'{TITLE_STATE}', get_options_active() ],

        ] ,
        "fields_form": [
#            ID/NAME          LABEL               PLACEHOLDER      TYPE         REQUIRED   ABLE/DISABLE   DATOS
            ['id',            'ID',               'ID',            'text',      False ,    False,         True ],
            ['titulo',      'Título',          'Título',      'text',     True ,     True  ,        None ],
            ['url',          'Url',             'Url', 'file', False,     True  ,        None ],
            ['preguntaid',  'Título de pregunta', 'Elegir pregunta', 'select', True ,True, [lambda: controlador_pregunta.get_options() , 'titulo_pre' ] ],
            ['descripcion', 'Descripción',     'Descripción', 'textarea', False,     True  ,        None ],
            #  ['activo',      f'{TITLE_STATE}',  'Activo',      'p',        True ,     False ,        None ],
        ],
        "crud_forms": {
            "crud_list": True ,
            "crud_search": True ,
            "crud_consult": True ,
            "crud_insert": True ,
            "crud_update": True ,
            "crud_delete": True ,
            "crud_unactive": False ,
        }
    },
}


REPORTES = {

}


def validar_error_crud():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                tabla = kwargs.get('tabla') or args[0]
                return rdrct_error(redirect_crud(tabla) , e)
        return wrapper
    return decorator



def redirect_url(url):
    return redirect(url_for(url))


def redirect_crud(tabla):
    return redirect(url_for('crud_generico', tabla = tabla))


def rdrct_error(resp_redirect , e):
    resp = make_response(resp_redirect)
    error_message = str(e)

    for clave in ERRORES:
        if clave in error_message:
            msg = ERRORES[clave]
            break
    else:
        msg =  'ERROR DESCONOCIDO ENCONTRADO: '+error_message

    resp.set_cookie('error', msg , max_age=30)
    return resp


def listar_cruds():
    pages = []

    if not CONTROLADORES:
        return pages
    for key, config in CONTROLADORES.items():
        if isinstance(config, dict) and config.get("active"):
            titulo = config.get("titulo", key).capitalize()
            icono_raw = config.get("icon_page")
            icono     = get_icon_page(icono_raw)
            pages.append([key, titulo, icono])

    return pages

@app.context_processor
def inject_globals():
    cruds = listar_cruds()
    options_pagination_crud, selected_option_crud = get_options_pagination_crud()
    return dict(
        CONTROLLERS           = cruds,
        cookie_error          = request.cookies.get('error'),

        # Paginación
        options_pagination_crud  = options_pagination_crud,
        selected_option_crud    = selected_option_crud,

        # Constantes
        URL_IMG_LOGO           = '/static/img/logousat.png',
        SYSTEM_NAME            = "chatbotUsatin",
        HABILITAR_ICON_PAGES   = HABILITAR_ICON_PAGES,
        STATE_0                = STATE_0,
        STATE_1                = STATE_1,
        ACT_STATE_0            = ACT_STATE_0,
        ACT_STATE_1            = ACT_STATE_1,
        NOMBRE_CRUD_PAGE       = NOMBRE_CRUD_PAGE,
        NOMBRE_ADMINPAGES_PAGE = NOMBRE_ADMINPAGES_PAGE,
        NOMBRE_OPTIONS_COL     = NOMBRE_OPTIONS_COL,
        NOMBRE_BTN_INSERT      = NOMBRE_BTN_INSERT,
        NOMBRE_BTN_UPDATE      = NOMBRE_BTN_UPDATE,
        NOMBRE_BTN_DELETE      = NOMBRE_BTN_DELETE,
        NOMBRE_BTN_UNACTIVE    = NOMBRE_BTN_UNACTIVE,
        NOMBRE_BTN_LIST        = NOMBRE_BTN_LIST,
        NOMBRE_BTN_CONSULT     = NOMBRE_BTN_CONSULT,
        NOMBRE_BTN_SEARCH      = NOMBRE_BTN_SEARCH,
        ICON_PAGE_CRUD         = ICON_PAGE_CRUD,
        ICON_PAGE_REPORT       = ICON_PAGE_REPORT,
        ICON_PAGE_DASHBOARD    = ICON_PAGE_DASHBOARD,
        ICON_PAGE_PANEL        = ICON_PAGE_PANEL,
        ICON_LIST              = ICON_LIST,
        ICON_CONSULT           = ICON_CONSULT,
        ICON_SEARCH            = ICON_SEARCH,
        ICON_INSERT            = ICON_INSERT,
        ICON_UPDATE            = ICON_UPDATE,
        ICON_DELETE            = ICON_DELETE,
        ICON_ACTIVE            = ICON_ACTIVE,
        ICON_UNACTIVE          = ICON_UNACTIVE,
        ICON_UNLOCK            = ICON_UNLOCK,
        ICON_PAGE_NOICON       = f'{ICON_PAGE_NOICON} d_i',
    )



@app.route("/crud=<tabla>")
def crud_generico(tabla):
    config = CONTROLADORES.get(tabla)
    if config:
        active = config["active"]
        no_crud = config.get('no_crud')
        if active is True and (no_crud is None or no_crud is False):
            icon_page_crud = get_icon_page(config.get("icon_page"))
            titulo = config["titulo"]
            controlador = config["controlador"]
            nombre_tabla = config["nombre_tabla"]
            filters = config["filters"]
            fields_form = config["fields_form"]

            existe_activo = controlador.exists_Activo()
            columnas , filas = controlador.get_table()
            primary_key = controlador.get_primary_key()
            table_columns  = list(filas[0].keys()) if filas else []
            CRUD_FORMS = config["crud_forms"]
            crud_list = CRUD_FORMS.get("crud_list")
            crud_search = CRUD_FORMS.get("crud_search")
            crud_consult = CRUD_FORMS.get("crud_consult")
            crud_insert = CRUD_FORMS.get("crud_insert")
            crud_update = CRUD_FORMS.get("crud_update")
            crud_delete = CRUD_FORMS.get("crud_delete")
            crud_unactive = CRUD_FORMS.get("crud_unactive") and existe_activo

            return render_template(
                "CRUD.html" ,
                tabla          = tabla ,
                nombre_tabla   = nombre_tabla ,
                icon_page_crud = icon_page_crud ,
                titulo         = titulo ,
                filas          = filas ,
                primary_key    = primary_key ,
                filters        = filters,
                fields_form    = fields_form ,
                # value_search   = value_search,
                columnas       = columnas ,
                key_columns    = list(columnas.keys()) ,
                table_columns  = table_columns ,
                # info_columns   = info_columns,
                crud_list      = crud_list,
                crud_search    = crud_search,
                crud_consult   = crud_consult,
                crud_insert    = crud_insert,
                crud_update    = crud_update,
                crud_delete    = crud_delete,
                crud_unactive  = crud_unactive,
            )


@app.route("/reporte=<report_name>")
def reporte(report_name):
    config = REPORTES.get(report_name)
    if config:
        active = config["active"]
        if active is True:
            titulo = config["titulo"]
            icon_page_crud = get_icon_page(config.get("icon_page"))
            nombre_tabla = config["nombre_tabla"]
            filters = config["filters"]
            columnas , filas = config["table"]
            table_columns  = list(filas[0].keys()) if filas else []

            return render_template(
                "CRUD.html" ,
                icon_page_crud = icon_page_crud ,
                titulo         = titulo ,
                filas          = filas ,
                filters        = filters,
                columnas       = columnas ,
                key_columns    = list(columnas.keys()) ,
                table_columns  = table_columns ,
                crud_search    = True,
                tabla = nombre_tabla,
                # crud_consult   = True,
                # crud_insert    = True,
                # crud_update    = True,
                # crud_delete    = True,
                crud_unactive  = True,
                esReporte      = True ,
            )


UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "static/docs"))
ALLOWED_EXTENSIONS = {'pdf', 'txt'}


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def extraer_texto_pdf(filepath, max_chars=1000):
    """
    Extrae texto limpio de un PDF para llenar automáticamente el campo descripcion.
    Limita a max_chars para evitar desbordes de campo.
    """
    try:
        texto = ""
        with fitz.open(filepath) as doc:
            for page in doc:
                texto += page.get_text()
                if len(texto) >= max_chars:
                    break
        texto = texto.strip().replace('\n', ' ')
        if len(texto) > max_chars:
            texto = texto[:max_chars] + "..."
        return texto
    except Exception as e:
        print(f"Error extrayendo texto del PDF: {e}")
        return ""

def guardar_archivo(archivo):
    if archivo and allowed_file(archivo.filename):
        filename = secure_filename(archivo.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        archivo.save(filepath)
        url = f"{filename}"
        return url, filepath
    return None, None

def guardar_archivo_2(archivo):
    print("Archivos recibidos:", request.files)  # Verifica que los archivos estén llegando correctamente
    
    if archivo:
        print(f"Nombre del archivo recibido: {archivo.filename}")
    
    if archivo and allowed_file(archivo.filename):
        filename = secure_filename(archivo.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # Imprime la ruta completa antes de guardar
        print("Ruta del archivo a guardar:", filepath)

        archivo.save(filepath)
        return filename, filepath  # Retorna nombre y ruta completa del archivo
    else:
        print("El archivo no es válido o no tiene extensión permitida.")
    
    return None, None


@app.route("/insert_row=<tabla>", methods=["POST"])
def crud_insert(tabla):
    # print("Tabla 0000", tabla)
    config = CONTROLADORES.get(tabla)
    if not config:
        return "Tabla no soportada", 404

    active = config["active"]
    no_crud = config.get("no_crud")

    if active is False:
        return "Tabla no soportada", 404

    controlador = config["controlador"]
    firma = inspect.signature(controlador.insert_row)

    valores = []
    filepath_archivo = None
    lector = clase_lectora_pdf.LectorArchivo()  # Usa tu clase con múltiples formatos

    for nombre, _ in firma.parameters.items():
        # print("Archivos recibidos:", request.files)  # Verifica que los archivos
        if nombre in request.files:
            print("Nombre del archivo:", request.files[nombre])
            archivo = request.files[nombre]
            if archivo.filename != "":
                if not lector.allowed_file(archivo.filename):
                    return "Tipo de archivo no permitido", 400
                nuevo_nombre, filepath_archivo = guardar_archivo_2(archivo)
                valores.append(nuevo_nombre)
            else:
                valores.append(request.form.get(f"{nombre}_actual"))
        else:
            valor = request.form.get(nombre)
            valores.append(valor)

    # print("Tabla ", tabla)
    if tabla == "documento":
        idx_desc = list(firma.parameters.keys()).index("descripcion")
        # print("Ruta del archivo00000:", filepath_archivo)
        if (valores[idx_desc] is None or valores[idx_desc].strip() == "") and filepath_archivo:
            print("Ruta del archivo:", filepath_archivo)

            texto_extraido = lector.leer(filepath_archivo)
            valores[idx_desc] = texto_extraido

    # print("Valores a insertar:", valores)
    controlador.insert_row(*valores)

    if no_crud:
        return redirect(url_for(no_crud))
    else:
        return redirect(url_for("crud_generico", tabla=tabla))

    

@app.route("/update_row=<tabla>", methods=["POST"])
def crud_update(tabla):
    config = CONTROLADORES.get(tabla)
    if not config:
        return "Tabla no soportada", 404

    active = config["active"]
    no_crud = config.get("no_crud")

    if active is False:
        return "Tabla no soportada", 404

    controlador = config["controlador"]
    firma = inspect.signature(controlador.update_row)

    valores = []
    for nombre, _ in firma.parameters.items():
        if nombre in request.files:
            archivo = request.files[nombre]
            if archivo.filename != "":
                nuevo_nombre = guardar_archivo(archivo)
                valores.append(nuevo_nombre)
            else:
                # Si no se selecciona una nueva imagen, mantener la actual
                valores.append(request.form.get(f"{nombre}_actual"))
        else:
            valor = request.form.get(nombre)
            valores.append(valor)

    controlador.update_row(*valores)

    if no_crud:
        return redirect(url_for(no_crud))
    else:
        return redirect(url_for("crud_generico", tabla=tabla))

# @app.route("/subir_y_leer", methods=["POST"])
# def subir_y_leer():
#     archivo = request.files.get("archivo")
#     if archivo:
#         lector = clase_lectora_pdf.LectorArchivo()
#         nombre_archivo, ruta = lector.guardar_archivo(archivo)
#         if ruta:
#             contenido = lector.leer(ruta)
#             print(f"Contenido del archivo {nombre_archivo}:\n{contenido}")
#             return jsonify({"archivo": nombre_archivo, "contenido": contenido})
#         return jsonify({"error": "Archivo no permitido"}), 400
#     return jsonify({"error": "No se recibió ningún archivo"}), 400


@app.route("/delete_row=<tabla>", methods=["POST"])
# @validar_empleado()
# @validar_error_crud()
def crud_delete(tabla):
    config = CONTROLADORES.get(tabla)
    if not config:
        return "Tabla no soportada", 404

    active = config["active"]
    no_crud = config.get('no_crud')

    if active is False:
        return "Tabla no soportada", 404

    controlador = config["controlador"]
    primary_key = controlador.get_primary_key()

    if isinstance(primary_key, list):
        valores_pk = [request.form.get(pk) for pk in primary_key]
        controlador.delete_row(*valores_pk)
    else:
        controlador.delete_row(request.form.get(primary_key))

    if no_crud :
        return redirect(url_for(no_crud))
    else:
        return redirect(url_for('crud_generico', tabla = tabla))


@app.route("/unactive_row=<tabla>", methods=["POST"])

def crud_unactive(tabla):
    config = CONTROLADORES.get(tabla)
    if not config:
        return "Tabla no soportada", 404

    active = config["active"]
    no_crud = config.get('no_crud')

    if active is False:
        return "Tabla no soportada", 404

    controlador = config["controlador"]
    existe_activo = controlador.exists_Activo()
    primary_key = controlador.get_primary_key()
    print(primary_key)

    if existe_activo:
        if isinstance(primary_key, list):
            valores_pk = [request.form.get(pk) for pk in primary_key]
            controlador.unactive_row(*valores_pk)
        else:
            controlador.unactive_row(request.form.get(primary_key))

    if no_crud :
        return redirect(url_for(no_crud))
    else:
        return redirect(url_for('crud_generico', tabla = tabla))

#########################################################
# @app.route("/dashboard")
# def dashboard_general():
#     return render_template("dashboard_general.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
