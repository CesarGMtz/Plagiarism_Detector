import ast
import re

analizar = lambda e: re.fullmatch(r'[\d+\-*/().\s]+', e) is not None

def es_seguro(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        nodos = list(ast.walk(tree))
        peligros = [ast.Call, ast.Name]
        return all(not isinstance(n, tuple(peligros)) for n in nodos)
    except:
        return False

def evaluar(expr):
    try:
        return eval(compile(ast.parse(expr, mode='eval'), '', 'eval'))
    except:
        return "Evaluación fallida"

def run():
    while True:
        entrada = input("Exp (salir para terminar): ").strip()
        if entrada.lower() == "salir":
            break

        if not analizar(entrada):
            print("Entrada inválida.")
            continue

        if not es_seguro(entrada):
            print("Riesgo detectado en la expresión.")
            continue

        print("Resultado:", evaluar(entrada))

run()

