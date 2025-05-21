import ast
import re

def revisar_caracteres(e):
    patron = r'^[0-9+\-*/(). \n\t]+$'
    return re.match(patron, e) is not None

def check_ast(e):
    try:
        t = ast.parse(e, mode='eval')
        for n in ast.walk(t):
            if isinstance(n, ast.Call) or isinstance(n, ast.Name):
                return False
        return True
    except:
        return False

def calcular(e):
    try:
        return eval(e)
    except:
        return "No se pudo evaluar"

def ejecutar_validador():
    e = input("Expresión matemática: ")
    if revisar_caracteres(e) and check_ast(e):
        print("Resultado:", calcular(e))
    else:
        print("Expresión inválida o peligrosa")

ejecutar_validador()

