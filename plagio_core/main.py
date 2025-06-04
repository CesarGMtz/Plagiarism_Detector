import os
import ast
import itertools
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from zipfile import ZipFile
from feature_extractor import extract_features_from_pair
from datetime import datetime

# === 1. Cargar y extraer el ZIP ===
zip_path = "codigos.zip"
extract_dir = "codigos_extraidos"

if not os.path.exists(zip_path):
    print(f" El archivo {zip_path} no existe.")
    exit()

with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# === 2. Buscar todos los .py ===
all_files = []
for root, _, files in os.walk(extract_dir):
    for f in files:
        if f.endswith(".py") and not f.startswith("._"):
            all_files.append(os.path.join(root, f))

if len(all_files) < 2:
    print(" Se necesitan al menos dos archivos .py")
    exit()

# === 3. Todos vs todos (permutaciones) ===
pares = list(itertools.permutations(all_files, 2))

# === 4. Extraer características ===
features_list = []
archivo1_list = []
archivo2_list = []

for archivo1, archivo2 in pares:
    try:
        features = extract_features_from_pair(archivo1, archivo2)
        features_list.append(features)
        archivo1_list.append(os.path.basename(archivo1))
        archivo2_list.append(os.path.basename(archivo2))
    except Exception as e:
        print(f"⚠️ Error con par {archivo1} - {archivo2}: {e}")

if not features_list:
    print(" No se extrajeron características.")
    exit()

df_features = pd.DataFrame(features_list)
df_features.insert(0, "archivo_1", archivo1_list)
df_features.insert(1, "archivo_2", archivo2_list)

# === 5. Cargar modelos entrenados ===
try:
    svm_model = joblib.load("modelo_SVM.joblib")
    svm_scaler = joblib.load("scaler_SVM.joblib")
    rf_model = joblib.load("modelo_RF.joblib")
    rf_scaler = joblib.load("scaler_RF.joblib")
except Exception as e:
    print(f"❌ Error al cargar modelos: {e}")
    exit()

# === 6. Clasificación binaria con SVM ===
try:
    X_bin = svm_scaler.transform(df_features.drop(columns=["archivo_1", "archivo_2"]))
    df_features["es_plagio"] = svm_model.predict(X_bin)
except Exception as e:
    print(f"❌ Error en clasificación binaria: {e}")
    exit()

# === 7. Clasificación multiclase con RF ===
try:
    X_tri = df_features[df_features["es_plagio"] == 1].drop(columns=["archivo_1", "archivo_2", "es_plagio"])
    if not X_tri.empty:
        X_tri_scaled = rf_scaler.transform(X_tri)
        df_features.loc[df_features["es_plagio"] == 1, "tipo_plagio_predicho"] = rf_model.predict(X_tri_scaled)
    else:
        df_features["tipo_plagio_predicho"] = 0
except Exception as e:
    print(f"❌ Error en clasificación triclase: {e}")
    df_features["tipo_plagio_predicho"] = 0

# === 8. Guardar en un solo archivo Excel ===
output_file = "resultado_clasificacion_unificado.xlsx"

if os.path.exists(output_file):
    df_existente = pd.read_excel(output_file)
else:
    df_existente = pd.DataFrame(columns=["archivo_1", "archivo_2", "es_plagio", "tipo_plagio_predicho"])

# Agregar evitando duplicados exactos
df_nuevo = df_features[["archivo_1", "archivo_2", "es_plagio", "tipo_plagio_predicho"]]
df_final = pd.concat([df_existente, df_nuevo]).drop_duplicates()

df_final.to_excel(output_file, index=False)
print(f"✅ Clasificación completada y guardada en: {output_file}")
