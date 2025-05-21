import ast
import re

def es_valida(expresion):
    patron = r'^[\d\+\-\*/\(\)\s]+$'
    return bool(re.match(patron, expresion))

def evaluar_expresion(expresion):
    try:
        arbol = ast.parse(expresion, mode='eval')
        return eval(compile(arbol, filename="", mode="eval"))
    except:
        return "Expresión inválida o peligrosa."

def pedir_entrada():
    return input("Ingresa una expresión matemática: ")

def main():
    while True:
        expr = pedir_entrada()
        if not es_valida(expr):
            print("Caracteres no permitidos.")
            continue
        resultado = evaluar_expresion(expr)
        print("Resultado:", resultado)
        if input("¿Salir? (s/n): ").lower() == "s":
            break

main()

