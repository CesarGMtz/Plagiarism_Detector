import ast
import re

FUNCIONES_PERMITIDAS = {"abs": abs, "round": round}

def validar_expresion(exp):
    regex = r'^[\d+\-*/().,\s]+$'
    return re.fullmatch(regex, exp) is not None

def tiene_elementos_peligrosos(arbol):
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Call):
            return True
        if isinstance(nodo, ast.Name) and nodo.id not in FUNCIONES_PERMITIDAS:
            return True
    return False

def procesar(exp):
    try:
        arbol = ast.parse(exp, mode='eval')
        if tiene_elementos_peligrosos(arbol):
            return "Expresión rechazada"
        return eval(compile(arbol, "", "eval"))
    except:
        return "Expresión no válida"

def main():
    expr = input("Introduce expresión: ")
    if validar_expresion(expr):
        print("Resultado:", procesar(expr))
    else:
        print("Caracteres inválidos")

main()

