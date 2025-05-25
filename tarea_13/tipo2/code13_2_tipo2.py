import ast
import re

def caracteres_validos(expr):
    return bool(re.match(r'^[0-9+\-*/(). \t\n]+$', expr))

def revisar_ast(expr):
    try:
        arbol = ast.parse(expr, mode='eval')
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.Call) or isinstance(nodo, ast.Name):
                return False
        return True
    except:
        return False

def calcular(expr):
    try:
        return eval(expr)
    except:
        return "Error al evaluar"

def iniciar():
    cadena = input("Ingresa una operación matemática: ")
    if caracteres_validos(cadena) and revisar_ast(cadena):
        print("Resultado:", calcular(cadena))
    else:
        print("Expresión no permitida")

iniciar()

