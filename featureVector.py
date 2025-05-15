import ast

from collections import Counter

class FeatureVector(ast.NodeVisitor):
    def __init__(self):
        self.features = Counter()

    def visit_FunctionDef(self, node):
        self.features["FunctionDef"] += 1
        self.generic_visit(node)

    def visit_BinOp(self, node):
        op_type = type(node.op)
        op_name = {
            ast.Add: '+',
            ast.Sub: '-',
            ast.Mult: '*',
            ast.Div: '/',
            ast.FloorDiv: '//',
            ast.Mod: '%',
            ast.Pow: '**',
            ast.LShift: '<<',
            ast.RShift: '>>',
            ast.BitOr: '|',
            ast.BitXor: '^',
            ast.BitAnd: '&',
            ast.MatMult: '@'
        }.get(op_type, str(op_type))
        self.features[f"BinOp:{op_name}"] += 1
        self.generic_visit(node)
    
    def visit_BoolOp(self, node):
        op_type = type(node.op)
        op_name = {
            ast.And: 'and',
            ast.Or: 'or',
        }.get(op_type, str(op_type))
        self.features[f"BoolOp:{op_name}"] += 1
        
    def visit_Compare(self, node):
        for op in node.ops:
            op_type = type(op)
            op_name = {
                ast.Eq: '==',
                ast.NotEq: '!=',
                ast.Lt: '<',
                ast.LtE: '<=',
                ast.Gt: '>',
                ast.GtE: '>=',
                ast.Is: 'is',
                ast.IsNot: 'is not',
                ast.In: 'in',
                ast.NotIn: 'not in',
            }.get(op_type, str(op_type))
            self.features[f"Cmp:{op_name}"] += 1
        self.generic_visit(node)
