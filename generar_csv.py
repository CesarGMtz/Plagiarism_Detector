import os
import csv
import ast
from collections import Counter
from featureVector import FeatureVector

BASE_DIRS = ["tarea_1", "tarea_2", "tarea_3","tarea_4","tarea_5","tarea_6","tarea_7","tarea_8","tarea_9","tarea_10","tarea_11", "tarea_12", "tarea_13","tarea_14","tarea_15","tarea_16","tarea_17","tarea_18","tarea_19","tarea_20"]  # Agrega aquí más tareas si las tienes
CATEGORIAS = ["tipo1", "tipo2", "tipo3", "noplagio"]

FIXED_KEYS = [
    'Assign', 'AugAssign', 'BinOp:+', 'BinOp:-', 'BinOp:*', 'BinOp:/', 'BinOp://', 'BinOp:%',
    'BoolOp:and', 'BoolOp:or',
    'Call', 'Cmp:==', 'Cmp:!=', 'Cmp:<', 'Cmp:<=', 'Cmp:>', 'Cmp:>=', 'Cmp:is', 'Cmp:is not', 'Cmp:in', 'Cmp:not in',
    'Dict', 'For', 'FunctionDef', 'If', 'IfElse', 'List', 'Name', 'Return', 'TotalArgs', 'Tuple', 'While',

    # Nuevas características para distinguir plagio tipo 2 vs 3
    'FunctionDepth',       # Profundidad máxima de funciones
    'NestedFunc',          # Funciones dentro de funciones
    'AvgFuncLength',       # Suma de líneas por función (puedes dividirla luego)
    'NestedIf',            # Ifs anidados dentro de otros if
]

def get_feature_vector(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    tree = ast.parse(code)
    extractor = FeatureVector()
    extractor.visit(tree)
    return extractor.features

def generate_csv():
    all_rows = []

    for BASE_DIR in BASE_DIRS:
        original_dir = os.path.join(BASE_DIR, "original")
        if not os.path.exists(original_dir):
            continue
        original_files = [f for f in os.listdir(original_dir) if f.endswith(".py")]

        for orig in original_files:
            path_orig = os.path.join(original_dir, orig)
            vec_orig = get_feature_vector(path_orig)

            for tipo in CATEGORIAS:
                tipo_path = os.path.join(BASE_DIR, tipo)
                if not os.path.exists(tipo_path):
                    continue
                if tipo == "noplagio":
                    # Compara con TODOS los de noplagio
                    tipo_files = [f for f in os.listdir(tipo_path) if f.endswith(".py")]
                else:
                    # Compara solo los que empiezan igual
                    tipo_files = [f for f in os.listdir(tipo_path) if f.endswith(".py") and f.startswith(orig.split(".py")[0])]

                for tf in tipo_files:
                    path_tf = os.path.join(tipo_path, tf)
                    vec_tf = get_feature_vector(path_tf)
                    diff = {k: abs(vec_orig.get(k, 0) - vec_tf.get(k, 0)) for k in FIXED_KEYS}
                    tipo_plagio = {"tipo1": 1, "tipo2": 2, "tipo3": 3, "noplagio": 0}[tipo]
                    row = {
                        "tarea": BASE_DIR,
                        "archivo_1": orig,
                        "archivo_2": tf,
                        "plagio_tipo": tipo_plagio
                    }
                    row.update(diff)
                    all_rows.append(row)

    fieldnames = ["tarea", "archivo_1", "archivo_2"] + FIXED_KEYS + ["plagio_tipo"]

    with open("Feature_Vector_CSV.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow({key: row.get(key, 0) for key in fieldnames})

if __name__ == "__main__":
    generate_csv()
