# === archivo: similitud.py ===
def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    if union == 0:
        return 1.0  # si ambos están vacíos, se consideran iguales
    return intersection / union


def extract_variable_names(source_code):
    import ast
    class VariableVisitor(ast.NodeVisitor):
        def __init__(self):
            self.variables = set()

        def visit_Name(self, node):
            self.variables.add(node.id)

    tree = ast.parse(source_code)
    visitor = VariableVisitor()
    visitor.visit(tree)
    return visitor.variables


def compute_jaccard_from_files(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1:
        code1 = f1.read()
    with open(file2, "r", encoding="utf-8") as f2:
        code2 = f2.read()

    vars1 = extract_variable_names(code1)
    vars2 = extract_variable_names(code2)

    return jaccard_similarity(vars1, vars2)
