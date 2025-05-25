import ast

def validar_ast(expr):
    try:
        nodo = ast.parse(expr, mode='eval')
        for elemento in ast.walk(nodo):
            if isinstance(elemento, (ast.Call, ast.Name)):
                return False
        return True
    except:
        return False

def procesar(expr):
    try:
        if validar_ast(expr):
            compilado = compile(ast.parse(expr, mode='eval'), '', 'eval')
            return eval(compilado)
        else:
            return "Expresión no segura"
    except:
        return "Error en la evaluación"

def ejecutar():
    while True:
        cadena = input("Escribe una operación (o 'salir'): ")
        if cadena.lower() == "salir":
            break
        print("Resultado:", procesar(cadena))

ejecutar()

