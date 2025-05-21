
import ast
import tokenize
from collections import Counter
from io import BytesIO

def count_comments(source_code):
    try:
        return sum(
            1 for tok in tokenize.tokenize(BytesIO(source_code.encode("utf-8")).readline)
            if tok.type == tokenize.COMMENT
        )
    except tokenize.TokenError:
        return 0

class FeatureVector(ast.NodeVisitor):
    def __init__(self, source_code=None):
        self.features = Counter()
        self.source_code = source_code
        if source_code:
            self.features["NumComments"] = count_comments(source_code)

    def visit_FunctionDef(self, node):
        self.features["FunctionDef"] += 1
        self.features["TotalArgs"] += len(node.args.args)

        # Calcular longitud total de cada función
        line_nums = []
        for child in ast.walk(node):
            if hasattr(child, "lineno"):
                line_nums.append(child.lineno)
        if line_nums:
            length = max(line_nums) - min(line_nums) + 1
            self.features["AvgFuncLength"] += length

        # Profundidad
        self.features["FunctionDepth"] = max(
            self.features.get("FunctionDepth", 0),
            self._compute_depth(node)
        )

        # Función anidada
        if any(isinstance(n, ast.FunctionDef) for n in ast.iter_child_nodes(node)):
            self.features["NestedFunc"] += 1

        self.generic_visit(node)

    def _compute_depth(self, node, level=1):
        max_depth = level
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.If, ast.While, ast.For)):
                max_depth = max(max_depth, self._compute_depth(child, level + 1))
        return max_depth

    def visit_Return(self, node):
        self.features["Return"] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        self.features["Call"] += 1
        self.generic_visit(node)

    def visit_Name(self, node):
        self.features["Name"] += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.features["Assign"] += 1
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.features["AugAssign"] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.features["For"] += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.features["While"] += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.features["If"] += 1
        if node.orelse:
            self.features["IfElse"] += 1
        if any(isinstance(child, ast.If) for child in node.body):
            self.features["NestedIf"] += 1
        self.generic_visit(node)

    def visit_Dict(self, node):
        self.features["Dict"] += 1
        self.generic_visit(node)

    def visit_Set(self, node):
        self.features["Set"] += 1
        self.generic_visit(node)

    def visit_List(self, node):
        self.features["List"] += 1
        self.generic_visit(node)

    def visit_Tuple(self, node):
        self.features["Tuple"] += 1
        self.generic_visit(node)

    def visit_BinOp(self, node):
        op_type = type(node.op)
        op_name = {
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
            ast.FloorDiv: "//",
            ast.Mod: "%",
            ast.Pow: "**",
            ast.LShift: "<<",
            ast.RShift: ">>",
            ast.BitOr: "|",
            ast.BitXor: "^",
            ast.BitAnd: "&",
            ast.MatMult: "@"
        }.get(op_type, str(op_type))
        self.features[f"BinOp:{op_name}"] += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        op_type = type(node.op)
        op_name = {
            ast.And: "and",
            ast.Or: "or",
        }.get(op_type, str(op_type))
        self.features[f"BoolOp:{op_name}"] += 1

    def visit_Compare(self, node):
        for op in node.ops:
            op_type = type(op)
            op_name = {
                ast.Eq: "==",
                ast.NotEq: "!=",
                ast.Lt: "<",
                ast.LtE: "<=",
                ast.Gt: ">",
                ast.GtE: ">=",
                ast.Is: "is",
                ast.IsNot: "is not",
                ast.In: "in",
                ast.NotIn: "not in",
            }.get(op_type, str(op_type))
            self.features[f"Cmp:{op_name}"] += 1
        self.generic_visit(node)
