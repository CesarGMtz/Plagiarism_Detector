import os
import csv
from featureVector import FeatureVector

BASE_DIRS = [f"tarea_{i}" for i in range(1, 21)]
CATEGORIAS = ["tipo1", "tipo2", "tipo3", "noplagio"]

FIXED_KEYS = [
    'Assign', 'AugAssign', 'BinOp:+', 'BinOp:-', 'BinOp:*', 'BinOp:/', 'BinOp://', 'BinOp:%',
    'BoolOp:and', 'BoolOp:or',
    'Call', 'Cmp:==', 'Cmp:!=', 'Cmp:<', 'Cmp:<=', 'Cmp:>', 'Cmp:>=', 'Cmp:is', 'Cmp:is not', 'Cmp:in', 'Cmp:not in',
    'Dict', 'For', 'FunctionDef', 'If', 'IfElse', 'List', 'Name', 'Return', 'TotalArgs', 'Tuple', 'While',
    'FunctionDepth', 'NestedFunc', 'AvgFuncLength', 'NestedIf',
    'var_name_jaccard', 'var_name_overlap', 'var_name_diff',
    'lex_common_tokens', 'lex_total_tokens_1', 'lex_total_tokens_2', 'lex_jaccard', 'lex_token_ratio',
    'lex_ngram_sim',
    'line_length_diff', 'literal_overlap', 'literal_jaccard',
'token_edit_ratio', 'call_sequence_similarity', 'num_funcs_1', 'num_funcs_2', 'func_count_diff', 'func_line_ratio_1', 'func_line_ratio_2', 'func_line_ratio_diff',
"tokens_per_func_diff", 'control_flow_sim','func_name_sequence_similarity'




]

def read_code(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_csv():
    all_rows = []

    for BASE_DIR in BASE_DIRS:
        original_dir = os.path.join(BASE_DIR, "original")
        if not os.path.exists(original_dir):
            continue
        original_files = [f for f in os.listdir(original_dir) if f.endswith(".py")]

        for orig in original_files:
            path_orig = os.path.join(original_dir, orig)
            code_orig = read_code(path_orig)

            for tipo in CATEGORIAS:
                tipo_path = os.path.join(BASE_DIR, tipo)
                if not os.path.exists(tipo_path):
                    continue

                if tipo == "noplagio":
                    tipo_files = [f for f in os.listdir(tipo_path) if f.endswith(".py")]
                else:
                    tipo_files = [f for f in os.listdir(tipo_path)
                                  if f.endswith(".py") and f.startswith(orig.split(".py")[0])]

                for tf in tipo_files:
                    path_tf = os.path.join(tipo_path, tf)
                    code_tf = read_code(path_tf)

                    fv = FeatureVector(code_orig, code_tf)
                    features = fv.extract()

                    row = {
                        "tarea": BASE_DIR,
                        "archivo_1": orig,
                        "archivo_2": tf,
                        "plagio_tipo": {"tipo1": 1, "tipo2": 2, "tipo3": 3, "noplagio": 0}[tipo]
                    }
                    for key in FIXED_KEYS:
                        row[key] = features.get(key, 0)

                    all_rows.append(row)

    fieldnames = ["tarea", "archivo_1", "archivo_2"] + FIXED_KEYS + ["plagio_tipo"]
    with open("Feature_Vector_CSV.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)

if __name__ == "__main__":
    generate_csv()
