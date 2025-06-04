import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
import zipfile
import shutil
import sys
from itertools import combinations
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

from feature_extractor import extract_features_from_pair 

logging.info("--- INICIO DEL SCRIPT ---")

if len(sys.argv) < 2:
    logging.error("Error: Debes proporcionar la ruta al archivo ZIP como argumento.")
    sys.exit(1)

zip_path = sys.argv[1]

current_script_dir = os.path.dirname(os.path.abspath(__file__))

temp_dir = os.path.join(current_script_dir, "temp_extraccion")
output_file = os.path.join(current_script_dir, "resultado_clasificacion_unificado.xlsx")

if not os.path.exists(zip_path):
    logging.error(f"Error: El archivo ZIP '{zip_path}' no existe en la ruta especificada.")
    sys.exit(1)

if os.path.exists(temp_dir):
    try:
        shutil.rmtree(temp_dir)
        logging.debug(f"Carpeta '{temp_dir}' eliminada exitosamente.")
    except OSError as e:
        logging.warning(f"Advertencia: No se pudo eliminar el directorio '{temp_dir}': {e}.")
os.makedirs(temp_dir, exist_ok=True)

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    logging.debug(f"Archivo ZIP '{zip_path}' extraído a '{temp_dir}'.")
except zipfile.BadZipFile:
    logging.error(f"Error: El archivo '{zip_path}' no es un archivo ZIP válido o está corrupto.")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    sys.exit(1)
except Exception as e:
    logging.error(f"Error inesperado al extraer el ZIP: {e}")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    sys.exit(1)

archivos_py = []
for root, _, files in os.walk(temp_dir):
    for file in files:
        if file.endswith(".py"):
            archivos_py.append(os.path.join(root, file))

logging.debug(f"Archivos .py encontrados en el ZIP (pruebas.py): {archivos_py}")
logging.debug(f"Número de archivos .py encontrados: {len(archivos_py)}")

if len(archivos_py) < 2:
    logging.error("Error: El archivo ZIP debe contener al menos 2 archivos .py para realizar comparaciones.")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    sys.exit(1)

try:
    models_and_scalers_paths = {
        "svm_model": os.path.join(current_script_dir, "modelo_SVM.joblib"),
        "svm_scaler": os.path.join(current_script_dir, "scaler_SVM.joblib"),
        "rf_model": os.path.join(current_script_dir, "modelo_RF.joblib"),
        "rf_scaler": os.path.join(current_script_dir, "scaler_RF.joblib"),
        "tipo3_model": os.path.join(current_script_dir, "modelo_Tipo3_vs_NoPlagio.joblib"),
        "tipo3_scaler": os.path.join(current_script_dir, "scaler_Tipo3_vs_NoPlagio.joblib"),
    }

    loaded_items = {}
    for name, path in models_and_scalers_paths.items():
        if not os.path.exists(path):
            logging.error(f"Error: El archivo '{os.path.basename(path)}' NO se encontró en la ruta esperada: {path}")
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            sys.exit(1)
        loaded_items[name] = joblib.load(path)

    svm_model = loaded_items["svm_model"]
    svm_scaler = loaded_items["svm_scaler"]
    rf_model = loaded_items["rf_model"]
    rf_scaler = loaded_items["rf_scaler"]
    tipo3_model = loaded_items["tipo3_model"]
    tipo3_scaler = loaded_items["tipo3_scaler"]

except Exception as e:
    logging.error(f"Error al cargar modelos y escaladores: {e}")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    sys.exit(1)

resultados = []
total_combinations = len(list(combinations(archivos_py, 2)))
logging.debug(f"Se esperan {total_combinations} combinaciones de archivos para comparar.")

for i, (archivo1_path, archivo2_path) in enumerate(combinations(archivos_py, 2)):
    archivo1_name = os.path.basename(archivo1_path)
    archivo2_name = os.path.basename(archivo2_path)
    logging.debug(f"Procesando combinación {i+1}/{total_combinations}: {archivo1_name} vs {archivo2_name}")

    features = {}
    try:
        extracted_features = extract_features_from_pair(archivo1_path, archivo2_path)
        if not isinstance(extracted_features, dict) or not extracted_features:
            logging.warning(f"Advertencia: No se extrajeron características válidas para {archivo1_name} y {archivo2_name}. Saltando.")
            df_features_pair = pd.DataFrame([{
                "archivo_1": archivo1_name,
                "archivo_2": archivo2_name,
                "plagio_predicho_binario": "Error Extracción Características",
                "tipo_plagio_predicho": "N/A",
                "porcentaje_tipo_plagio": -1.0,
                "sospecha_tipo3_%": -1.0
            }])
            resultados.append(df_features_pair)
            continue
        features = extracted_features
    except Exception as e:
        logging.error(f"Error al extraer características entre {archivo1_name} y {archivo2_name}: {e}.")
        df_features_pair = pd.DataFrame([{
            "archivo_1": archivo1_name,
            "archivo_2": archivo2_name,
            "plagio_predicho_binario": f"Error: {e}",
            "tipo_plagio_predicho": "N/A",
            "porcentaje_tipo_plagio": -1.0,
            "sospecha_tipo3_%": -1.0
        }])
        resultados.append(df_features_pair)
        continue

    df_features_pair = pd.DataFrame([features])
    df_features_pair.insert(0, "archivo_1", archivo1_name)
    df_features_pair.insert(1, "archivo_2", archivo2_name)

    try:
        cols_for_svm = [col for col in df_features_pair.columns if col not in ["archivo_1", "archivo_2"]]
        X_bin_df = df_features_pair[cols_for_svm]

        missing_svm_cols = set(svm_scaler.feature_names_in_) - set(X_bin_df.columns)
        if missing_svm_cols:
            logging.error(f"Error: Columnas faltantes para SVM: {missing_svm_cols}.")
            raise ValueError("Columnas SVM incompletas")

        X_bin_df = X_bin_df[svm_scaler.feature_names_in_] 
        X_bin = svm_scaler.transform(X_bin_df)
        df_features_pair["plagio_predicho_binario"] = svm_model.predict(X_bin)[0]
    except Exception as e:
        logging.error(f"Error en clasificación binaria entre {archivo1_name} y {archivo2_name}: {e}.")
        df_features_pair["plagio_predicho_binario"] = "Error_Binario"
        df_features_pair["tipo_plagio_predicho"] = "N/A"
        df_features_pair["porcentaje_tipo_plagio"] = -1.0
        df_features_pair["sospecha_tipo3_%"] = -1.0
        resultados.append(df_features_pair)
        continue

    try:
        if df_features_pair["plagio_predicho_binario"].iloc[0] == 1:
            cols_for_rf = [col for col in df_features_pair.columns if col not in ["archivo_1", "archivo_2", "plagio_predicho_binario"]]
            X_tri_df = df_features_pair[cols_for_rf]

            missing_rf_cols = set(rf_scaler.feature_names_in_) - set(X_tri_df.columns)
            if missing_rf_cols:
                logging.error(f"Error: Columnas faltantes para RF: {missing_rf_cols}.")
                raise ValueError("Columnas RF incompletas")

            X_tri_df = X_tri_df[rf_scaler.feature_names_in_]
            X_tri_scaled = rf_scaler.transform(X_tri_df)

            tipo = rf_model.predict(X_tri_scaled)[0]
            probs = rf_model.predict_proba(X_tri_scaled)[0]
            prob_dict = dict(zip(rf_model.classes_, probs))
            porcentaje_tipo = round(prob_dict.get(tipo, 0) * 100, 2)

            df_features_pair["tipo_plagio_predicho"] = int(tipo)
            df_features_pair["porcentaje_tipo_plagio"] = porcentaje_tipo
        else:
            df_features_pair["tipo_plagio_predicho"] = 0
            df_features_pair["porcentaje_tipo_plagio"] = 0.0
    except Exception as e:
        logging.error(f"Error en clasificación triclase entre {archivo1_name} y {archivo2_name}: {e}.")
        df_features_pair["tipo_plagio_predicho"] = "Error_Triclase"
        df_features_pair["porcentaje_tipo_plagio"] = -1.0

    try:
        if df_features_pair["plagio_predicho_binario"].iloc[0] == 0:
            cols_for_tipo3 = [col for col in df_features_pair.columns if col not in [
                "archivo_1", "archivo_2", "plagio_predicho_binario",
                "tipo_plagio_predicho", "porcentaje_tipo_plagio"
            ]]
            X_tipo3check_df = df_features_pair[cols_for_tipo3]

            missing_tipo3_cols = set(tipo3_scaler.feature_names_in_) - set(X_tipo3check_df.columns)
            if missing_tipo3_cols:
                logging.error(f"Error: Columnas faltantes para Tipo 3: {missing_tipo3_cols}.")
                raise ValueError("Columnas Tipo 3 incompletas")

            X_tipo3check_df = X_tipo3check_df[tipo3_scaler.feature_names_in_]
            X_tipo3check = tipo3_scaler.transform(X_tipo3check_df)
            probs_tipo3 = tipo3_model.predict_proba(X_tipo3check)[:, 1] * 100
            df_features_pair["sospecha_tipo3_%"] = np.round(probs_tipo3[0], 2)
        else:
            df_features_pair["sospecha_tipo3_%"] = 0.0
    except Exception as e:
        logging.error(f"No se pudo calcular sospecha tipo 3 entre {archivo1_name} y {archivo2_name}: {e}.")
        df_features_pair["sospecha_tipo3_%"] = -1.0

    resultados.append(df_features_pair)

logging.debug(f"Número final de DataFrames en la lista 'resultados': {len(resultados)}")

if resultados:
    try:
        df_total = pd.concat(resultados, ignore_index=True)

        df_total['Predicción: ¿Es plagio?'] = df_total['plagio_predicho_binario'].map({
            1: 'Sí ✔',
            0: 'No ✘',
            'Error_Binario': 'Error',
            'Error Extracción Características': 'Error'
        }).fillna(df_total['plagio_predicho_binario'])

        df_total['Tipo de Plagio Predicho'] = df_total['tipo_plagio_predicho'].map({
            1: 'Tipo 1',
            2: 'Tipo 2',
            3: 'Tipo 3',
            0: 'N/A'
        }).fillna(df_total['tipo_plagio_predicho'])

        df_total['Sospecha Tipo 3'] = df_total['sospecha_tipo3_%'].apply(
            lambda x: f"{x:.2f}%" if isinstance(x, (int, float)) and x != -1 else ('N/A' if x == -1 else str(x))
        )
        df_total['Porcentaje Plagio'] = df_total['porcentaje_tipo_plagio'].apply(
            lambda x: f"{x:.2f}%" if isinstance(x, (int, float)) and x != -1 else ('N/A' if x == -1 else str(x))
        )

        df_final_excel = df_total[[
            "archivo_1",
            "archivo_2",
            "Predicción: ¿Es plagio?",
            "Tipo de Plagio Predicho",
            "Sospecha Tipo 3",
            "Porcentaje Plagio"
        ]].rename(columns={
            "archivo_1": "Archivo de Origen",
            "archivo_2": "Archivo a Comparar"
        })

        # --- INICIO DEL BLOQUE DE ORDENAMIENTO ---
        orden_plagio = pd.CategoricalDtype(
            categories=['Sí ✔', 'Error', 'No ✘'], 
            ordered=True
        )
        df_final_excel['Predicción: ¿Es plagio?'] = df_final_excel['Predicción: ¿Es plagio?'].astype(orden_plagio)

        df_final_excel['Porcentaje Plagio Numerico'] = df_final_excel['Porcentaje Plagio'].str.replace('%', '').replace('N/A', np.nan).replace('Error', np.nan).astype(float)
        df_final_excel['Sospecha Tipo 3 Numerico'] = df_final_excel['Sospecha Tipo 3'].str.replace('%', '').replace('N/A', np.nan).replace('Error', np.nan).astype(float)

        df_final_excel = df_final_excel.sort_values(
            by=[
                'Predicción: ¿Es plagio?', 
                'Porcentaje Plagio Numerico', 
                'Sospecha Tipo 3 Numerico',
                'Archivo de Origen'
            ], 
            ascending=[
                True,
                False,
                False,
                True
            ],
            ignore_index=True
        )
        
        df_final_excel = df_final_excel.drop(columns=['Porcentaje Plagio Numerico', 'Sospecha Tipo 3 Numerico'])

        # --- FIN DEL BLOQUE DE ORDENAMIENTO ---

        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        df_final_excel.to_excel(output_file, index=False)
        logging.debug(f"Archivo Excel '{output_file}' guardado/actualizado exitosamente.")
    except Exception as e:
        logging.error(f"Error al guardar el archivo Excel '{output_file}': {e}")
else:
    logging.info("No se generaron resultados de comparación.")

try:
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        logging.debug(f"Carpeta temporal '{temp_dir}' eliminada al finalizar.")
except OSError as e:
    logging.error(f"Error al eliminar la carpeta temporal '{temp_dir}': {e}.")

logging.info("--- PROCESO DE DETECCIÓN DE PLAGIO COMPLETADO ---")