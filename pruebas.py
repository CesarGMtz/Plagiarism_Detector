import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
from feature_extractor import extract_features_from_pair

# === 1. Leer dos archivos de una carpeta ===
directorio = "codesss"
archivos_py = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith(".py") and not f.startswith("._")]

if len(archivos_py) != 2:
    print(" Debes tener exactamente 2 archivos .py dentro de la carpeta 'codesss'.")
    exit()

# Ordenar alfabéticamente para mantener un orden constante
archivo1, archivo2 = sorted(archivos_py)

# === 2. Extraer características del par ===
try:
    features = extract_features_from_pair(archivo1, archivo2)
except Exception as e:
    print(f"Error al extraer características del par: {e}")
    exit()

df_features = pd.DataFrame([features])
df_features.insert(0, "archivo_1", os.path.basename(archivo1))
df_features.insert(1, "archivo_2", os.path.basename(archivo2))

# === 3. Cargar modelos y escaladores ===
try:
    svm_model = joblib.load("modelo_SVM.joblib")
    svm_scaler = joblib.load("scaler_SVM.joblib")
    rf_model = joblib.load("modelo_RF.joblib")
    rf_scaler = joblib.load("scaler_RF.joblib")
    tipo3_model = joblib.load("modelo_Tipo3_vs_NoPlagio.joblib")
    tipo3_scaler = joblib.load("scaler_Tipo3_vs_NoPlagio.joblib")
except Exception as e:
    print(f" Error al cargar modelos: {e}")
    exit()

# === 4. Clasificación binaria con SVM ===
try:
    X_bin = svm_scaler.transform(df_features.drop(columns=["archivo_1", "archivo_2"]))
    df_features["plagio_predicho_binario"] = svm_model.predict(X_bin)
except Exception as e:
    print(f" Error en clasificación binaria: {e}")
    exit()

# === 5. Clasificación multiclase con RF + porcentaje del tipo ===
try:
    if df_features["plagio_predicho_binario"].iloc[0] == 1:
        X_tri = df_features.drop(columns=["archivo_1", "archivo_2", "plagio_predicho_binario"])
        X_tri_scaled = rf_scaler.transform(X_tri)

        tipo = rf_model.predict(X_tri_scaled)[0]
        probs = rf_model.predict_proba(X_tri_scaled)[0]
        prob_dict = dict(zip(rf_model.classes_, probs))
        porcentaje_tipo = round(prob_dict.get(tipo, 0) * 100, 2)

        df_features["tipo_plagio_predicho"] = tipo
        df_features["porcentaje_tipo_plagio"] = porcentaje_tipo
    else:
        df_features["tipo_plagio_predicho"] = 0
        df_features["porcentaje_tipo_plagio"] = 0.0
except Exception as e:
    print(f" Error en clasificación triclase: {e}")
    df_features["tipo_plagio_predicho"] = 0
    df_features["porcentaje_tipo_plagio"] = 0.0

# === 6. Calcular sospecha de tipo 3 aunque sea no plagio ===
try:
    no_plagio_rows = df_features["plagio_predicho_binario"] == 0
    if no_plagio_rows.any():
        X_tipo3check = tipo3_scaler.transform(
            df_features[no_plagio_rows].drop(columns=[
                "archivo_1", "archivo_2", "plagio_predicho_binario",
                "tipo_plagio_predicho", "porcentaje_tipo_plagio"
            ])
        )
        probs_tipo3 = tipo3_model.predict_proba(X_tipo3check)[:, 1] * 100
        df_features.loc[no_plagio_rows, "sospecha_tipo3_%"] = np.round(probs_tipo3, 2)
    else:
        df_features["sospecha_tipo3_%"] = 0.0
except Exception as e:
    print(f"⚠️ No se pudo calcular sospecha tipo 3: {e}")
    df_features["sospecha_tipo3_%"] = -1

# === 7. Guardar en un único Excel acumulativo ===
output_file = "resultado_clasificacion_unificado.xlsx"

if os.path.exists(output_file):
    df_existente = pd.read_excel(output_file)
else:
    df_existente = pd.DataFrame(columns=[
        "archivo_1", "archivo_2", "plagio_predicho_binario", 
        "tipo_plagio_predicho", "porcentaje_tipo_plagio", "sospecha_tipo3_%"
    ])

df_nuevo = df_features[[
    "archivo_1", "archivo_2", "plagio_predicho_binario",
    "tipo_plagio_predicho", "porcentaje_tipo_plagio", "sospecha_tipo3_%"
]]
df_final = pd.concat([df_existente, df_nuevo]).drop_duplicates()

df_final.to_excel(output_file, index=False)
print(f" Comparación completada: {os.path.basename(archivo1)} vs {os.path.basename(archivo2)}")
