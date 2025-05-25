# svm_tipo3_vs_noplagio.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carga el CSV 
df = pd.read_csv("Feature_Vector_CSV.csv")

# 2. Filtra solo los casos de tipo 3 y no plagio 
df = df[df["plagio_tipo"].isin([0, 3])]

# Etiqueta: 0 = No Plagio, 1 = Tipo 3
df["etiqueta"] = df["plagio_tipo"].apply(lambda x: 1 if x == 3 else 0)

# 3. Preparar X e y
X = df.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea", "etiqueta"], errors="ignore")
y = df["etiqueta"]

#  4. Dividir en conjunto de entrenamiento y prueba 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# 5. Escalado 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#  6. Entrenar modelo SVM (kernel RBF) 
svm_model = SVC(kernel="rbf", C=1.0, gamma="scale", class_weight="balanced", probability=True, random_state=42)
svm_model.fit(X_train_scaled, y_train)

# 7. Evaluar en entrenamiento 
y_train_pred = svm_model.predict(X_train_scaled)
print("=== Resultados de ENTRENAMIENTO ===")
print(f"Exactitud: {accuracy_score(y_train, y_train_pred):.4f}")
print(classification_report(y_train, y_train_pred, target_names=["No Plagio", "Tipo 3"]))

# 8. Evaluar en prueba 
y_test_pred = svm_model.predict(X_test_scaled)
print("=== Resultados de PRUEBA ===")
print(f"Exactitud: {accuracy_score(y_test, y_test_pred):.4f}")
print(classification_report(y_test, y_test_pred, target_names=["No Plagio", "Tipo 3"]))

#  9. Matriz de Confusión (prueba) 
cm = confusion_matrix(y_test, y_test_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No Plagio", "Tipo 3"], yticklabels=["No Plagio", "Tipo 3"])
plt.title("Matriz de Confusión - Tipo 3 vs No Plagio (SVM)")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

#  10. Guardar modelo y scaler 
joblib.dump(svm_model, "modelo_Tipo3_vs_NoPlagio.joblib")
joblib.dump(scaler, "scaler_Tipo3_vs_NoPlagio.joblib")
print("Modelo y scaler guardados.")
