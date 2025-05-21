import re
import ast

PERMITIDOS = {"abs": abs, "round": round}

def caracteres_validos(expr):
    return bool(re.fullmatch(r'[0-9+\-*/().,\s]+', expr))

def evaluacion_segura(expresion):
    try:
        arbol = ast.parse(expresion, mode='eval')
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.Call):
                return "Error: llamada a función no permitida"
            elif isinstance(nodo, ast.Name):
                if nodo.id not in PERMITIDOS:
                    return "Error: variable no permitida"
        return eval(compile(arbol, '', 'eval'))
    except Exception as e:
        return f"Error de ejecución: {str(e)}"

def ejecutar():
    entrada = input("Introduce una expresión matemática: ")
    if caracteres_validos(entrada):
        print("Resultado:", evaluacion_segura(entrada))
    else:
        print("Expresión con caracteres inválidos")

if __name__ == "__main__":
    ejecutar()

