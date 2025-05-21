import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

# === 1. Cargar CSV ===
df = pd.read_csv("Feature_Vector_CSV.csv")

X = df.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea"], errors="ignore")
y = df["plagio_tipo"]

# === 2. Separar datos ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)

# === 3. Escalado ===
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === 4. Entrenar modelo Naive Bayes ===
model = GaussianNB()
model.fit(X_train_scaled, y_train)

# === 5. Guardar modelo y escalador ===
joblib.dump(model, "modelo_naivebayes.pkl")
joblib.dump(scaler, "scaler.pkl")

# === 6. Predicciones ===
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

# === 7. Resultados de Entrenamiento ===
print("\n=== RESULTADOS ENTRENAMIENTO ===")
print("Precisión:", accuracy_score(y_train, y_pred_train))
print("Precisión macro:", precision_score(y_train, y_pred_train, average='macro'))
print("\nReporte de Clasificación:\n")
print(classification_report(y_train, y_pred_train, target_names=["No Plagio (0)", "Tipo 1", "Tipo 2", "Tipo 3"]))

# === 8. Resultados de Prueba ===
print("\n=== RESULTADOS PRUEBA ===")
print("Precisión:", accuracy_score(y_test, y_pred_test))
print("Precisión macro:", precision_score(y_test, y_pred_test, average='macro'))
print("\nReporte de Clasificación:\n")
print(classification_report(y_test, y_pred_test, target_names=["No Plagio (0)", "Tipo 1", "Tipo 2", "Tipo 3"]))
