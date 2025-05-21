import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

# === 1. Cargar CSV ===
df = pd.read_csv("Feature_Vector_CSV.csv")

df["es_plagio"] = df["plagio_tipo"].apply(lambda x: 0 if x == 0 else 1)

X = df.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea", "es_plagio"], errors="ignore")
y = df["es_plagio"]

# === 2. Separar datos ===
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# === 3. Escalado ===
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === 4. Entrenar modelo Naive Bayes ===
model = GaussianNB()
model.fit(X_train_scaled, y_train)

# === 6. Predicciones ===
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

# === 7. Resultados de Entrenamiento ===
print("\n=== RESULTADOS ENTRENAMIENTO ===")
print("Exactitud:", accuracy_score(y_train, y_pred_train))
print("Precisión macro:", precision_score(y_train, y_pred_train, average='macro'))
print("Recall macro:", recall_score(y_train, y_pred_train, average='macro'))
print("\nReporte de Clasificación:\n")
print(classification_report(y_train, y_pred_train, target_names=["No Plagio", "Plagio"]))

# === 8. Resultados de Prueba ===
print("\n=== RESULTADOS PRUEBA ===")
print("Exactitud:", accuracy_score(y_test, y_pred_test))
print("Precisión macro:", precision_score(y_test, y_pred_test, average='macro'))
print("Recall macro:", recall_score(y_train, y_pred_train, average='macro'))
print("\nReporte de Clasificación:\n")
print(classification_report(y_test, y_pred_test, target_names=["No Plagio", "Plagio"]))
