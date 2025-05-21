import ast

def analizar(expresion):
    try:
        tree = ast.parse(expresion, mode='eval')
    except:
        return False, "Expresión inválida"

    for nodo in ast.walk(tree):
        if isinstance(nodo, ast.Call) or isinstance(nodo, ast.Name):
            return False, "Uso de funciones o nombres no permitidos"

    return True, tree

def evaluar_arbol(tree):
    try:
        return eval(compile(tree, '', 'eval'))
    except:
        return "Error durante la evaluación"

def iniciar():
    while True:
        e = input("Expr (escribe salir para terminar): ")
        if e.strip().lower() == "salir":
            break
        valido, resultado = analizar(e)
        if valido:
            print("Resultado:", evaluar_arbol(resultado))
        else:
            print("Error:", resultado)

iniciar()

