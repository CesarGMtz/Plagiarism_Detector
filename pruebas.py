import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from feature_extractor import extract_features_from_pair

# === 1. Leer dos archivos de una carpeta ===
directorio = "codesss"
archivos_py = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith(".py") and not f.startswith("._")]

if len(archivos_py) != 2:
    print("❌ Debes tener exactamente 2 archivos .py dentro de la carpeta 'codigos_prueba'.")
    exit()

archivo1, archivo2 = archivos_py

# === 2. Extraer características del par ===
try:
    features = extract_features_from_pair(archivo1, archivo2)
except Exception as e:
    print(f"❌ Error al extraer características del par: {e}")
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
except Exception as e:
    print(f"❌ Error al cargar modelos: {e}")
    exit()

# === 4. Clasificación binaria con SVM ===
try:
    X_bin = svm_scaler.transform(df_features.drop(columns=["archivo_1", "archivo_2"]))
    df_features["plagio_predicho_binario"] = svm_model.predict(X_bin)
except Exception as e:
    print(f"❌ Error en clasificación binaria: {e}")
    exit()

# === 5. Clasificación multiclase con RF ===
try:
    X_tri = df_features[df_features["plagio_predicho_binario"] == 1].drop(columns=["archivo_1", "archivo_2", "plagio_predicho_binario"])
    if not X_tri.empty:
        X_tri_scaled = rf_scaler.transform(X_tri)
        tipos = rf_model.predict(X_tri_scaled)
        df_features.loc[df_features["plagio_predicho_binario"] == 1, "tipo_plagio_predicho"] = tipos
    df_features.loc[df_features["plagio_predicho_binario"] == 0, "tipo_plagio_predicho"] = 0
except Exception as e:
    print(f"❌ Error en clasificación triclase: {e}")
    df_features["tipo_plagio_predicho"] = 0

# === 6. Guardar en un único Excel acumulativo ===
output_file = "resultado_clasificacion_unificado.xlsx"

if os.path.exists(output_file):
    df_existente = pd.read_excel(output_file)
else:
    df_existente = pd.DataFrame(columns=["archivo_1", "archivo_2", "plagio_predicho_binario", "tipo_plagio_predicho"])

df_nuevo = df_features[["archivo_1", "archivo_2", "plagio_predicho_binario", "tipo_plagio_predicho"]]
df_final = pd.concat([df_existente, df_nuevo]).drop_duplicates()

df_final.to_excel(output_file, index=False)
print(f"✅ Comparación y clasificación completada entre: {os.path.basename(archivo1)} y {os.path.basename(archivo2)}")
