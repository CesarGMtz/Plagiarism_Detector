def validar_expresion(expr):
    simbolos = set("0123456789+-*/(). ")
    return all(c in simbolos for c in expr)

def ejecutar_expresion(expr):
    try:
        return eval(expr, {"__builtins__": None}, {})
    except Exception:
        return "Expresión inválida"

def main():
    while True:
        linea = input("Expr matemática (q para salir): ")
        if linea.lower() == 'q':
            break
        if not validar_expresion(linea):
            print("Contiene caracteres prohibidos.")
        else:
            print("Resultado:", ejecutar_expresion(linea))

main()

