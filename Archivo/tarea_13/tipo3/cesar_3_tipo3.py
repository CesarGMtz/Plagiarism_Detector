import ast

def verificar_seguridad(expr):
    try:
        arbol = ast.parse(expr, mode='eval')
        for nodo in ast.walk(arbol):
            if not isinstance(nodo, (ast.Expression, ast.BinOp, ast.Num, ast.Add, ast.Sub, ast.Mult, ast.Div)):
                return False
        return True
    except:
        return False

def evaluar(expr):
    return eval(compile(ast.parse(expr, mode='eval'), filename="", mode="eval"))

def main():
    while True:
        entrada = input("Ingresa una expresión matemática segura: ")
        if verificar_seguridad(entrada):
            print("Resultado:", evaluar(entrada))
        else:
            print("Expresión no segura.")
        if input("¿Finalizar? (s/n): ").lower() == "s":
            break

main()

