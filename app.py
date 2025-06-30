
# @app.route("/api/sql", methods=["POST"])
# def api_sql():
#     try:
#         data = request.get_json()
#         tipo = data.get("tipo")  # "fetchall", "fetchone", "execute", "execute_last_id"
#         sql = data.get("sql")
#         args = data.get("args", [])

#         if not tipo or not sql:
#             return jsonify({"error": "Faltan parámetros obligatorios: 'tipo' y 'sql'"}), 400

#         conn = bd.obtener_conexion()
#         cursor = conn.cursor()

#         if tipo == "fetchall":
#             cursor.execute(sql, args)
#             result = cursor.fetchall()
#             conn.close()
#             return jsonify(result)

#         elif tipo == "fetchone":
#             cursor.execute(sql, args)
#             result = cursor.fetchone()
#             conn.close()
#             return jsonify(result)

#         elif tipo == "execute":
#             cursor.execute(sql, args)
#             conn.commit()
#             conn.close()
#             return jsonify({"status": "ok"})

#         elif tipo == "execute_last_id":
#             cursor.execute(sql, args)
#             last_id = cursor.lastrowid
#             conn.commit()
#             conn.close()
#             return jsonify({"status": "ok", "last_id": last_id})

#         else:
#             conn.close()
#             return jsonify({"error": "Tipo de operación inválido"}), 400

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route("/api/mensajes", methods=["GET"])
# def get_mensajes():
#     lista = controlador.get_table()
#     return jsonify(lista)


# @app.route("/get_historial")
# def get_historial():
#     data = bd.sql_select_fetchall('select * from historial order by fecha desc')
#     return data


# @app.route("/")
# @app.route("/get_webhook")
# def get_webhook():
#     data = bd.sql_select_fetchall('select * from webhook order by fecha desc')
#     texto = ''
#     for msg in data:
#         if msg['dato'] :
#             m = force_json(msg['dato'])["entry"][0]["changes"][0]["value"]["messages"][0]
#             texto += f'''<p>{m}</p>'''

#     return f'{texto}'



# @app.route("/subir_documento", methods=["POST"])
# def subir_documento():
#     if request.method == "POST":
#         titulo = request.form["titulo"]
#         archivo = request.files["file"]

#         if archivo and allowed_file(archivo.filename):
#             filename = secure_filename(archivo.filename)
#             filepath = os.path.join(UPLOAD_FOLDER, filename)
#             archivo.save(filepath)

#             # texto = extraer_texto_con_pdfco(filepath)
#             texto = filepath
#             # descripcion = gpt.generar_descripcion_con_gpt(texto)
#             url = f"https://franckcv.pythonanywhere.com/static/docs/{filename}"

#             sql = """
#                 INSERT INTO documento (titulo, url, descripcion)
#                 VALUES (%s, %s, %s)
#             """
#             bd.sql_execute(sql, [titulo, url, texto])



