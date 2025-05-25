import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# 1. Cargar el CSV 
df = pd.read_csv("Feature_Vector_CSV.csv")

# 2. Convertir a binario: 0 = no plagio, 1 = cualquier tipo de plagio 
df["es_plagio"] = df["plagio_tipo"].apply(lambda x: 0 if x == 0 else 1)

# 3. Preparar X (atributos) e y (clase binaria) 
X = df.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea", "es_plagio"], errors="ignore")
y = df["es_plagio"]

# 4. División de datos 
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# 5. Escalado 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Entrenamiento con Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train_scaled, y_train)

# 7. Guardar modelo y escalador 
joblib.dump(nb_model, "modelo_NB.joblib")
joblib.dump(scaler, "scaler_NB.joblib")

# 8. Predicciones 
y_train_pred = nb_model.predict(X_train_scaled)
y_test_pred = nb_model.predict(X_test_scaled)

# 9. Resultados
print("=== Resultados de Entrenamiento ===")
print("Exactitud:", accuracy_score(y_train, y_train_pred))
print("Precisión macro:", precision_score(y_train, y_train_pred, average='macro'))
print("Recall macro:", recall_score(y_train, y_train_pred, average='macro'))
print("Reporte de Clasificación:\n", classification_report(y_train, y_train_pred, target_names=["No Plagio", "Plagio"]))

print("\n=== Resultados de Prueba ===")
print("Exactitud:", accuracy_score(y_test, y_test_pred))
print("Precisión macro:", precision_score(y_test, y_test_pred, average='macro'))
print("Recall macro:", recall_score(y_test, y_test_pred, average='macro'))
print("Reporte de Clasificación:\n", classification_report(y_test, y_test_pred, target_names=["No Plagio", "Plagio"]))

# 10. Matriz de Confusión 
cm = confusion_matrix(y_test, y_test_pred)
labels = ["No Plagio", "Plagio"]

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", xticklabels=labels, yticklabels=labels)
plt.title("Matriz de Confusión - Naive Bayes (Plagio vs No Plagio)")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.tight_layout()
plt.show()
