from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import uuid
import shutil
import subprocess
import logging

app = Flask(__name__)
logging.basicConfig(filename='flask_app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

UPLOAD_ZIP_DIR = 'uploaded_zips_temp'
os.makedirs(UPLOAD_ZIP_DIR, exist_ok=True)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PLAGIO_CORE_PATH = os.path.join(PROJECT_ROOT, "plagio_core")
PRUEBAS_SCRIPT_PATH = os.path.join(PLAGIO_CORE_PATH, "pruebas.py")
OUTPUT_EXCEL_PATH = os.path.join(PLAGIO_CORE_PATH, "resultado_clasificacion_unificado.xlsx")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'zipfile' not in request.files:
        logging.warning("No se envió archivo en la solicitud de subida.")
        return "No se envió archivo", 400

    zipf = request.files['zipfile']
    if zipf.filename == '':
        logging.warning("Archivo ZIP vacío o sin nombre.")
        return "Archivo ZIP vacío o sin nombre", 400

    unique_filename = f"{uuid.uuid4()}_{zipf.filename}"
    uploaded_zip_absolute_path = os.path.join(PROJECT_ROOT, UPLOAD_ZIP_DIR, unique_filename)

    try:
        zipf.save(uploaded_zip_absolute_path)
        logging.info(f"Archivo ZIP '{zipf.filename}' guardado temporalmente en '{uploaded_zip_absolute_path}'")

        result = subprocess.run(
            ["python", PRUEBAS_SCRIPT_PATH, uploaded_zip_absolute_path],
            cwd=PLAGIO_CORE_PATH,
            capture_output=True,
            text=True,
            check=True
        )
        logging.info("pruebas.py stdout:\n" + result.stdout)
        logging.info("pruebas.py stderr:\n" + result.stderr)

    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar pruebas.py (código {e.returncode}):")
        logging.error("Stdout:\n" + e.stdout)
        logging.error("Stderr:\n" + e.stderr)
        return f"Error en el análisis. Consulte los logs del servidor para más detalles. Detalles del script: {e.stderr}", 500
    except Exception as e:
        logging.error(f"Error inesperado durante la subida o ejecución: {e}", exc_info=True)
        return f"Error interno del servidor: {str(e)}", 500
    finally:
        if os.path.exists(uploaded_zip_absolute_path):
            try:
                os.remove(uploaded_zip_absolute_path)
                logging.info(f"Archivo ZIP temporal eliminado: {uploaded_zip_absolute_path}")
            except Exception as e:
                logging.error(f"Error al eliminar el archivo ZIP temporal '{uploaded_zip_absolute_path}': {e}")

    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/get_excel')
def get_excel():
    if not os.path.exists(OUTPUT_EXCEL_PATH):
        logging.error(f"Solicitud de Excel, pero el archivo no existe: {OUTPUT_EXCEL_PATH}")
        return "Archivo de resultados no encontrado. Por favor, realice un análisis primero.", 404
    
    return send_from_directory(PLAGIO_CORE_PATH, 'resultado_clasificacion_unificado.xlsx')
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)