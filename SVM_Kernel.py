import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
import joblib

# 1. Carga el CSV y filtra solo los casos de plagio (tipo 1, 2, 3) 
df = pd.read_csv("Feature_Vector_CSV.csv")
df_plagio = df[df["plagio_tipo"] != 0]  # Solo plagios reales

# 2. Prepara X (atributos) e y (tipo de plagio) 
X = df_plagio.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea"], errors="ignore")
y = df_plagio["plagio_tipo"]

# 3. División de datos 
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

#  4. Escalado 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Entrena modelo SVM con kernel RBF 
model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
model.fit(X_train_scaled, y_train)

#  6. Guardar modelo y escalador para uso futuro 
joblib.dump(model, "modelo_svm_trinary.pkl")
joblib.dump(scaler, "scaler_trinary.pkl")

#  7. Evaluación 
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

print("=== Resultados de Entrenamiento ===")
print("Precisión:", accuracy_score(y_train, y_train_pred))
print("Precisión macro:", precision_score(y_train, y_train_pred, average='macro'))
print("Reporte de Clasificación:\n", classification_report(y_train, y_train_pred, target_names=["Tipo 1", "Tipo 2", "Tipo 3"]))

print("\n=== Resultados de Prueba ===")
print("Precisión:", accuracy_score(y_test, y_test_pred))
print("Precisión macro:", precision_score(y_test, y_test_pred, average='macro'))
print("Reporte de Clasificación:\n", classification_report(y_test, y_test_pred, target_names=["Tipo 1", "Tipo 2", "Tipo 3"]))

# 8. Matriz de Confusión 
cm = confusion_matrix(y_test, y_test_pred, labels=[1, 2, 3])
labels = ["Tipo 1", "Tipo 2", "Tipo 3"]

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.title("Matriz de Confusión - Clasificador por Tipo de Plagio (SVM)")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.tight_layout()
plt.show()
