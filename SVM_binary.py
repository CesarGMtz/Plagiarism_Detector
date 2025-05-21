import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv("Feature_Vector_CSV.csv")

# Convertir a binario: 0 = no plagio, 1 = cualquier tipo de plagio
df["es_plagio"] = df["plagio_tipo"].apply(lambda x: 0 if x == 0 else 1)

# Preparar X (atributos) e y (clase binaria)
X = df.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea", "es_plagio"], errors="ignore")
y = df["es_plagio"]

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrenamiento con SVM
svm_model = SVC(kernel="sigmoid", probability=True, random_state=42)
svm_model.fit(X_train_scaled, y_train)

# Predicciones
y_train_pred = svm_model.predict(X_train_scaled)
y_test_pred = svm_model.predict(X_test_scaled)

# Resultados
print("=== Resultados de Entrenamiento ===")
print("Precisión:", accuracy_score(y_train, y_train_pred))
print("Precision macro:", precision_score(y_train, y_train_pred, average='macro'))
print("Reporte de Clasificación:\n", classification_report(y_train, y_train_pred, target_names=["No Plagio", "Plagio"]))

print("\n=== Resultados de Prueba ===")
print("Precisión:", accuracy_score(y_test, y_test_pred))
print("Precision macro:", precision_score(y_test, y_test_pred, average='macro'))
print("Reporte de Clasificación:\n", classification_report(y_test, y_test_pred, target_names=["No Plagio", "Plagio"]))

# Matriz de Confusión
cm = confusion_matrix(y_test, y_test_pred)
labels = ["No Plagio", "Plagio"]

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.title("Matriz de Confusión - SVM")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.tight_layout()
plt.show()
