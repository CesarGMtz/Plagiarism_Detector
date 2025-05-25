import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix, f1_score
import joblib

#  1. Carga el CSV y filtrar solo casos con plagio (tipo 1, 2, 3)
df = pd.read_csv("Feature_Vector_CSV.csv")
df_plagio = df[df["plagio_tipo"] != 0]

#  2. Se preparan los datos 
X = df_plagio.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea"], errors="ignore")
y = df_plagio["plagio_tipo"]

#  3. División de datos 
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# 4. Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Entrenamiento del modelo Random Forest con class_weight 
model = RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42)
model.fit(X_train_scaled, y_train)

"""#  6. Validación cruzada 
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring="f1_macro")
print(f"F1 macro (validación cruzada): {cv_scores.mean():.4f}")"""

# 7. Guardar modelo y escalador
joblib.dump(model, "modelo_RF.joblib")
joblib.dump(scaler, "scaler_RF.joblib")
print("Modelo y escalador guardados como 'modelo_RF.joblib' y 'scaler_RF.joblib'.")

# 8. Evaluación 
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

# 9. Matriz de Confusión 
cm = confusion_matrix(y_test, y_test_pred, labels=[1, 2, 3])
labels = ["Tipo 1", "Tipo 2", "Tipo 3"]

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", xticklabels=labels, yticklabels=labels)
plt.title("Matriz de Confusión - Clasificador por Tipo de Plagio (Random Forest)")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.tight_layout()
plt.show()

# 10. Importancia de Features 
importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=feature_names)
plt.title("Importancia de Features (Random Forest)")
plt.tight_layout()
plt.show()
