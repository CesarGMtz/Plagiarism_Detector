import ast
import tokenize
import difflib
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

def extract_variable_names(tree):
    return {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}

def variable_name_similarity(tree1, tree2):
    names1 = extract_variable_names(tree1)
    names2 = extract_variable_names(tree2)
    intersection = names1.intersection(names2)
    union = names1.union(names2)
    jaccard = len(intersection) / len(union) if union else 1.0
    overlap = len(intersection)
    total_diff = len(union) - overlap
    return {
        "var_name_jaccard": jaccard,
        "var_name_overlap": overlap,
        "var_name_diff": total_diff
    }

def extract_literals(tree):
    return {n.value for n in ast.walk(tree) if isinstance(n, ast.Constant)}

def extract_call_names(tree):
    return [n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
def extract_control_flow_sequence(tree):
    sequence = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            sequence.append("if")
        elif isinstance(node, ast.For):
            sequence.append("for")
        elif isinstance(node, ast.While):
            sequence.append("while")
        elif isinstance(node, ast.FunctionDef):
            sequence.append("def")
        elif isinstance(node, ast.Call):
            sequence.append("call")
        elif isinstance(node, ast.Return):
            sequence.append("return")
    return sequence

def control_flow_similarity(tree1, tree2):
    seq1 = extract_control_flow_sequence(tree1)
    seq2 = extract_control_flow_sequence(tree2)
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    return matcher.ratio()
def ngram_similarity(tokens1, tokens2, n=3):
    def get_ngrams(tokens, n):
        return set(tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1))
    ngrams1 = get_ngrams(tokens1, n)
    ngrams2 = get_ngrams(tokens2, n)
    intersection = ngrams1.intersection(ngrams2)
    union = ngrams1.union(ngrams2)
    return len(intersection) / len(union) if union else 1.0

def lexical_similarity(code1, code2):
    try:
        tokens1 = [
            tok.string for tok in tokenize.tokenize(BytesIO(code1.encode("utf-8")).readline)
            if tok.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT}
        ]
        tokens2 = [
            tok.string for tok in tokenize.tokenize(BytesIO(code2.encode("utf-8")).readline)
            if tok.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT}
        ]

        set1, set2 = set(tokens1), set(tokens2)
        common = set1.intersection(set2)
        union = set1.union(set2)

        return {
            "lex_common_tokens": len(common),
            "lex_total_tokens_1": len(set1),
            "lex_total_tokens_2": len(set2),
            "lex_jaccard": len(common) / len(union) if union else 1.0,
            "lex_token_ratio": len(common) / len(tokens1) if tokens1 else 0.0,
            "lex_ngram_sim": ngram_similarity(tokens1, tokens2),
            "line_length_diff": abs(len(tokens1) - len(tokens2)),
            "token_edit_ratio": difflib.SequenceMatcher(None, tokens1, tokens2).ratio()
        }

    except tokenize.TokenError:
        return {
            "lex_common_tokens": 0,
            "lex_total_tokens_1": 0,
            "lex_total_tokens_2": 0,
            "lex_jaccard": 0.0,
            "lex_token_ratio": 0.0,
            "lex_ngram_sim": 0.0,
            "line_length_diff": 0,
            "token_edit_ratio": 0.0
        }

class FeatureVector(ast.NodeVisitor):
    def __init__(self, source_code1=None, source_code2=None):
        self.features = Counter()
        self.source_code1 = source_code1
        self.source_code2 = source_code2
        self.tree1 = ast.parse(source_code1) if source_code1 else None
        self.tree2 = ast.parse(source_code2) if source_code2 else None

        if source_code1:
            self.features["NumComments_1"] = count_comments(source_code1)
        if source_code2:
            self.features["NumComments_2"] = count_comments(source_code2)

    def extract(self):
        if self.tree1:
            self.visit(self.tree1)
        if self.tree2:
            self.visit(self.tree2)

        sim = variable_name_similarity(self.tree1, self.tree2)
        self.features["var_name_jaccard"] = sim["var_name_jaccard"]
        self.features["var_name_overlap"] = sim["var_name_overlap"]
        self.features["var_name_diff"] = sim["var_name_diff"]

        if self.source_code1 and self.source_code2:
            lex = lexical_similarity(self.source_code1, self.source_code2)
            for key, value in lex.items():
                self.features[key] = value

            # Literals
            literals1 = extract_literals(self.tree1)
            literals2 = extract_literals(self.tree2)
            literal_common = literals1.intersection(literals2)
            literal_union = literals1.union(literals2)
            self.features["literal_overlap"] = len(literal_common)
            self.features["literal_jaccard"] = len(literal_common) / len(literal_union) if literal_union else 1.0

            # Calls
            calls1 = extract_call_names(self.tree1)
            calls2 = extract_call_names(self.tree2)
            seq = difflib.SequenceMatcher(None, calls1, calls2)
            self.features["call_sequence_similarity"] = seq.ratio()

            # Funciones definidas
            funcs1 = len([n for n in ast.walk(self.tree1) if isinstance(n, ast.FunctionDef)])
            funcs2 = len([n for n in ast.walk(self.tree2) if isinstance(n, ast.FunctionDef)])
            self.features["num_funcs_1"] = funcs1
            self.features["num_funcs_2"] = funcs2
            self.features["func_count_diff"] = abs(funcs1 - funcs2)
            # Similaridad del orden de nombres de funciones
            def get_func_names(tree):
                return [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]

            func_names1 = get_func_names(self.tree1)
            func_names2 = get_func_names(self.tree2)
            seq_func = difflib.SequenceMatcher(None, func_names1, func_names2)
            self.features["func_name_sequence_similarity"] = seq_func.ratio()
            # Promedio de tokens por función (tipo 3 tiende a muchas funciones pequeñas)
            tokens1 = [
                tok.string for tok in tokenize.tokenize(BytesIO(self.source_code1.encode("utf-8")).readline)
                if tok.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT}
            ]
            tokens2 = [
                tok.string for tok in tokenize.tokenize(BytesIO(self.source_code2.encode("utf-8")).readline)
                if tok.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT}
            ]
            tokens_per_func_1 = len(tokens1) / funcs1 if funcs1 else 0
            tokens_per_func_2 = len(tokens2) / funcs2 if funcs2 else 0
            self.features["tokens_per_func_diff"] = abs(tokens_per_func_1 - tokens_per_func_2)

            # Proporción de líneas en funciones vs total
            total_lines_1 = len(self.source_code1.strip().splitlines())
            total_lines_2 = len(self.source_code2.strip().splitlines())

            func_lines_1 = sum(
                max([child.lineno for child in ast.walk(n) if hasattr(child, "lineno")], default=n.lineno) - n.lineno + 1
                for n in ast.walk(self.tree1) if isinstance(n, ast.FunctionDef)
            )
            func_lines_2 = sum(
                max([child.lineno for child in ast.walk(n) if hasattr(child, "lineno")], default=n.lineno) - n.lineno + 1
                for n in ast.walk(self.tree2) if isinstance(n, ast.FunctionDef)
            )

            self.features["func_line_ratio_1"] = func_lines_1 / total_lines_1 if total_lines_1 else 0
            self.features["func_line_ratio_2"] = func_lines_2 / total_lines_2 if total_lines_2 else 0
            self.features["func_line_ratio_diff"] = abs(self.features["func_line_ratio_1"] - self.features["func_line_ratio_2"])
            # Similaridad de flujo de control
            self.features["control_flow_sim"] = control_flow_similarity(self.tree1, self.tree2)

        return self.features


    def visit_FunctionDef(self, node):
        self.features["FunctionDef"] += 1
        self.features["TotalArgs"] += len(node.args.args)

        line_nums = [child.lineno for child in ast.walk(node) if hasattr(child, "lineno")]
        if line_nums:
            length = max(line_nums) - min(line_nums) + 1
            self.features["AvgFuncLength"] += length

        self.features["FunctionDepth"] = max(
            self.features.get("FunctionDepth", 0),
            self._compute_depth(node)
        )

        if any(isinstance(n, ast.FunctionDef) for n in ast.iter_child_nodes(node)):
            self.features["NestedFunc"] += 1

        self.generic_visit(node)

    def _compute_depth(self, node, level=1):
        return max((self._compute_depth(child, level + 1)
                    for child in ast.iter_child_nodes(node)
                    if isinstance(child, (ast.FunctionDef, ast.If, ast.While, ast.For))), default=level)

    def visit_Return(self, node): self.features["Return"] += 1; self.generic_visit(node)
    def visit_Call(self, node): self.features["Call"] += 1; self.generic_visit(node)
    def visit_Name(self, node): self.features["Name"] += 1; self.generic_visit(node)
    def visit_Assign(self, node): self.features["Assign"] += 1; self.generic_visit(node)
    def visit_AugAssign(self, node): self.features["AugAssign"] += 1; self.generic_visit(node)
    def visit_For(self, node): self.features["For"] += 1; self.generic_visit(node)
    def visit_While(self, node): self.features["While"] += 1; self.generic_visit(node)

    def visit_If(self, node):
        self.features["If"] += 1
        if node.orelse: self.features["IfElse"] += 1
        if any(isinstance(child, ast.If) for child in node.body): self.features["NestedIf"] += 1
        self.generic_visit(node)

    def visit_Dict(self, node): self.features["Dict"] += 1; self.generic_visit(node)
    def visit_Set(self, node): self.features["Set"] += 1; self.generic_visit(node)
    def visit_List(self, node): self.features["List"] += 1; self.generic_visit(node)
    def visit_Tuple(self, node): self.features["Tuple"] += 1; self.generic_visit(node)

    def visit_BinOp(self, node):
        op_name = {
            ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.FloorDiv: "//",
            ast.Mod: "%", ast.Pow: "**", ast.LShift: "<<", ast.RShift: ">>", ast.BitOr: "|",
            ast.BitXor: "^", ast.BitAnd: "&", ast.MatMult: "@"
        }.get(type(node.op), str(type(node.op)))
        self.features[f"BinOp:{op_name}"] += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        op_name = {ast.And: "and", ast.Or: "or"}.get(type(node.op), str(type(node.op)))
        self.features[f"BoolOp:{op_name}"] += 1

    def visit_Compare(self, node):
        for op in node.ops:
            op_name = {
                ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=",
                ast.Gt: ">", ast.GtE: ">=", ast.Is: "is", ast.IsNot: "is not",
                ast.In: "in", ast.NotIn: "not in"
            }.get(type(op), str(type(op)))
            self.features[f"Cmp:{op_name}"] += 1
        self.generic_visit(node)
