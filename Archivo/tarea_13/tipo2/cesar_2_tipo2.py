import re
import ast

def entrada_valida(expr):
    patron = r'^[\d\s+\-*/().]+$'
    return re.fullmatch(patron, expr) is not None

def seguridad(expr):
    try:
        nodo = ast.parse(expr, mode='eval')
        elementos = list(ast.walk(nodo))
        if any(isinstance(n, (ast.Call, ast.Name)) for n in elementos):
            return False
        return True
    except:
        return False

def ejecutar_eval(expr):
    try:
        return eval(expr)
    except:
        return "Error en ejecución"

def correr_validador():
    texto = input("Expresión matemática segura: ")
    if not entrada_valida(texto):
        print("Contiene símbolos no permitidos.")
        return

    if not seguridad(texto):
        print("Expresión potencialmente peligrosa.")
        return

    print("Resultado final:", ejecutar_eval(texto))

if __name__ == "__main__":
    correr_validador()

