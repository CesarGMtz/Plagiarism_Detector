import ast

from collections import Counter

class FeatureVector(ast.NodeVisitor):
    def __init__(self):
        self.features = Counter()

    # FUNCTION
    def visit_FunctionDef(self, node):
        self.features["FunctionDef"] += 1
        num_args = len(node.args.args)
        self.features["TotalArgs"] += num_args
        self.generic_visit(node)
    
    def visit_Return(self, node):
        self.features["Return"] += 1
        self.generic_visit(node)
    
    def visit_Call(self, node):
        self.features["Call"] += 1
        self.generic_visit(node)

    # VARIABLES
    def visit_Name(self, node):
        self.features["Name"] += 1
        self.generic_visit(node)
        
    def visit_Assign(self, node):
        self.features["Assign"] += 1
        self.generic_visit(node)
        
    def visit_AugAssign(self, node):
        self.features["AugAssign"] += 1
        self.generic_visit(node)
        
    # CONTROL
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
        self.generic_visit(node)
    
    # STRUCTURES
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
    
    # OPERATORS
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
