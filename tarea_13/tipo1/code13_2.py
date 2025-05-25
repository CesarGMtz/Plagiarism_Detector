import ast
import re

def validar_caracteres(expresion):
    return bool(re.match(r'^[0-9+\-*/(). \t\n]+$', expresion))

def analizar_ast(expresion):
    try:
        nodo = ast.parse(expresion, mode='eval')
        for subnodo in ast.walk(nodo):
            if isinstance(subnodo, ast.Call):
                return False
            if isinstance(subnodo, ast.Name):
                return False
        return True
    except:
        return False

def evaluar(expresion):
    try:
        return eval(expresion)
    except:
        return "Error en evaluación"

def main():
    expresion = input("Expresión: ")
    if validar_caracteres(expresion) and analizar_ast(expresion):
        print("Resultado:", evaluar(expresion))
    else:
        print("Expresión no segura")

main()

