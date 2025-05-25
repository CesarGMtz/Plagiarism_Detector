import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Cargar el CSV nuevamente
df = pd.read_csv("Feature_Vector_CSV.csv")
df_plagio = df[df["plagio_tipo"].isin([1, 2, 3])]

# Preparar X (vectores de diferencia) e y (etiqueta)
X = df_plagio.drop(columns=["archivo_1", "archivo_2", "plagio_tipo", "tarea"], errors="ignore")
y_true = df_plagio["plagio_tipo"]

# Clasificador manual implementado como función
def clasificar_manual(diff_row):
    if all(diff_row.get(k, 0) == 0 for k in [
        "AvgFuncLength", "LinesInFunctions", "Name", "TotalLines"
    ]):
        return 1
    if (
        diff_row.get("AvgFuncLength", 0) < 3 and
        diff_row.get("LinesInFunctions", 0) < 3 and
        diff_row.get("Name", 0) < 5 and
        diff_row.get("TotalLines", 0) < 5
    ):
        return 2
    if (
        diff_row.get("AvgFuncLength", 0) >= 5 or
        diff_row.get("LinesInFunctions", 0) >= 5 or
        diff_row.get("Name", 0) >= 5 or
        diff_row.get("TotalLines", 0) >= 6
    ):
        return 3
    return -1

# Aplicar la función a todos los ejemplos
y_pred = X.apply(clasificar_manual, axis=1)

# Reporte de clasificación
report = classification_report(y_true, y_pred, labels=[1, 2, 3], target_names=["Tipo 1", "Tipo 2", "Tipo 3"])
report
