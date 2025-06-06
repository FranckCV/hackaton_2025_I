# controladores/controlador_dashboard.py
from controladores.bd import obtener_conexion
from datetime import datetime

def obtener_datos_dashboard():
    """Obtiene todos los datos necesarios para el dashboard"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    datos = {}
    
    try:
        # 1. Total de categorías
        cursor.execute("SELECT COUNT(*) FROM categoria")
        datos['total_categorias'] = cursor.fetchone()[0]
        
        # 2. Categorías activas
        cursor.execute("SELECT COUNT(*) FROM categoria WHERE activo = 1")
        datos['categorias_activas'] = cursor.fetchone()[0]
        
        # 3. Total de preguntas
        cursor.execute("SELECT COUNT(*) FROM pregunta")
        datos['total_preguntas'] = cursor.fetchone()[0]
        
        # 4. Total de registros en historial
        cursor.execute("SELECT COUNT(*) FROM historial")
        datos['total_historial'] = cursor.fetchone()[0]
        
        # 5. Total de palabras clave
        cursor.execute("SELECT COUNT(*) FROM palabra_clave")
        datos['total_palabras_clave'] = cursor.fetchone()[0]
        
        # 6. Interacciones de hoy
        hoy = datetime.now().strftime('%Y-%m-%d')
        cursor.execute("SELECT COUNT(*) FROM historial WHERE DATE(fecha) = %s", (hoy,))
        datos['interacciones_hoy'] = cursor.fetchone()[0]
        
        # 7. Lista de categorías con su estado
        cursor.execute("SELECT nombre, activo FROM categoria ORDER BY nombre")
        categorias_raw = cursor.fetchall()
        datos['categorias'] = []
        for cat in categorias_raw:
            datos['categorias'].append({
                'nombre': cat[0],
                'activo': cat[1]
            })
        
        # 8. Preguntas por categoría
        cursor.execute("""
            SELECT c.nombre, COUNT(p.id) as cantidad
            FROM categoria c
            LEFT JOIN pregunta p ON c.id = p.CATEGORIAid
            WHERE c.activo = 1
            GROUP BY c.nombre
            ORDER BY cantidad DESC
        """)
        preguntas_por_cat = cursor.fetchall()
        datos['preguntas_por_categoria'] = []
        for item in preguntas_por_cat:
            datos['preguntas_por_categoria'].append({
                'categoria': item[0],
                'cantidad': item[1]
            })
        
        # 9. Actividad reciente (últimos 5 registros del historial)
        cursor.execute("""
            SELECT mensaje, fecha 
            FROM historial 
            ORDER BY fecha DESC 
            LIMIT 5
        """)
        actividad_raw = cursor.fetchall()
        datos['actividad_reciente'] = []
        for actividad in actividad_raw:
            datos['actividad_reciente'].append({
                'mensaje': actividad[0],
                'fecha': actividad[1]
            })
        
        # 10. Cálculos adicionales
        if datos['categorias_activas'] > 0:
            datos['promedio_preguntas_categoria'] = round(datos['total_preguntas'] / datos['categorias_activas'], 1)
        else:
            datos['promedio_preguntas_categoria'] = 0
            
        if datos['total_preguntas'] > 0:
            datos['promedio_palabras_pregunta'] = round(datos['total_palabras_clave'] / datos['total_preguntas'], 1)
        else:
            datos['promedio_palabras_pregunta'] = 0
        
        # 11. Última interacción
        cursor.execute("SELECT MAX(fecha) FROM historial")
        ultima_fecha = cursor.fetchone()[0]
        datos['ultima_interaccion'] = ultima_fecha
        
        # 12. Fecha actual para el dashboard
        datos['fecha_actual'] = datetime.now()
        
    except Exception as e:
        print(f"Error obteniendo datos del dashboard: {e}")
        # Datos por defecto en caso de error
        datos = {
            'total_categorias': 0,
            'categorias_activas': 0,
            'total_preguntas': 0,
            'total_historial': 0,
            'total_palabras_clave': 0,
            'interacciones_hoy': 0,
            'categorias': [{'nombre': 'Error cargando datos', 'activo': 0}],
            'preguntas_por_categoria': [{'categoria': 'Error', 'cantidad': 0}],
            'actividad_reciente': [{'mensaje': 'Error cargando actividad', 'fecha': datetime.now()}],
            'promedio_preguntas_categoria': 0,
            'promedio_palabras_pregunta': 0,
            'ultima_interaccion': None,
            'fecha_actual': datetime.now()
        }
    
    finally:
        cursor.close()
        conexion.close()
    
    return datos