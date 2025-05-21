import ast

def validar(exp):
    try:
        tree = ast.parse(exp, mode='eval')
        for n in ast.walk(tree):
            if type(n) in (ast.Call, ast.Name):
                return False
        return True
    except:
        return False

def evaluar(exp):
    try:
        if validar(exp):
            return eval(compile(ast.parse(exp, mode='eval'), '', 'eval'))
        return "Expresión no segura"
    except:
        return "Error de evaluación"

def programa():
    while True:
        dato = input(">> ")
        if dato.lower() == "salir":
            break
        print("Salida:", evaluar(dato))

programa()

