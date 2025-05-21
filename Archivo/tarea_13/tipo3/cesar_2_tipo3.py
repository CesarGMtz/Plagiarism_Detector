import re
import ast
import operator

OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def evaluar_seguro(expr):
    try:
        nodo = ast.parse(expr, mode='eval')
        return _evaluar_nodo(nodo.body)
    except Exception:
        return "Error de sintaxis."

def _evaluar_nodo(nodo):
    if isinstance(nodo, ast.BinOp):
        izq = _evaluar_nodo(nodo.left)
        der = _evaluar_nodo(nodo.right)
        op = OPERADORES[type(nodo.op)]
        return op(izq, der)
    elif isinstance(nodo, ast.Num):
        return nodo.n
    raise TypeError("Expresión no válida")

def leer_expr():
    return input("Expresión para evaluar: ")

def ciclo():
    while True:
        expr = leer_expr()
        print("Resultado:", evaluar_seguro(expr))
        if input("¿Salir? (s/n): ").lower() == "s":
            break

ciclo()

