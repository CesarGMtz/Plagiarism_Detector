import ast

def es_valido(exp):
    try:
        arbol = ast.parse(exp, mode='eval')
        for nodo in ast.walk(arbol):
            if isinstance(nodo, (ast.Call, ast.Name)):
                return False
        return True
    except:
        return False

def evaluar_seguro(exp):
    try:
        if es_valido(exp):
            return eval(compile(ast.parse(exp, mode='eval'), '', 'eval'))
        else:
            return "Expresión peligrosa"
    except:
        return "Error en la expresión"

def main():
    while True:
        entrada = input("Ingresa una expresión (o salir): ")
        if entrada.lower() == "salir":
            break
        print("Resultado:", evaluar_seguro(entrada))

main()

