import re
import ast

def sanitizar(exp):
    return exp.replace(" ", "")

def validar_tokens(exp):
    permitidos = set("0123456789+-*/().")
    return all(char in permitidos for char in exp)

def revisar_ast(exp):
    try:
        arbol = ast.parse(exp, mode='eval')
        nodos = list(ast.walk(arbol))
        return not any(isinstance(n, (ast.Call, ast.Name)) for n in nodos)
    except:
        return False

def evaluar(exp):
    try:
        return eval(exp)
    except:
        return "Error al evaluar"

def iniciar_validador():
    expr = input("Evalúa esta expresión matemática segura: ")
    expr = sanitizar(expr)

    if not validar_tokens(expr):
        print("Expresión contiene símbolos no válidos.")
        return

    if not revisar_ast(expr):
        print("Expresión rechazada por seguridad.")
        return

    print("Resultado:", evaluar(expr))

iniciar_validador()

