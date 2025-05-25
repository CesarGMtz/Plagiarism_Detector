import re
import ast
import operator

FUNCIONES_PERMITIDAS = {"abs": abs, "round": round}

def expresion_valida(exp):
    permitidos = re.compile(r'^[0-9+\-*/()., \t\n]+$')
    return bool(permitidos.match(exp))

def evaluar_seguro(exp):
    try:
        nodo = ast.parse(exp, mode='eval')
        for sub in ast.walk(nodo):
            if isinstance(sub, ast.Call):
                return "Error: No se permiten llamadas a funciones"
            elif isinstance(sub, ast.Name):
                if sub.id not in FUNCIONES_PERMITIDAS:
                    return f"Error: Nombre no autorizado ({sub.id})"
        return eval(compile(nodo, '<string>', mode='eval'))
    except Exception as error:
        return f"Error: {str(error)}"

def iniciar():
    expresion = input("Introduce una operación matemática: ")
    if expresion_valida(expresion):
        salida = evaluar_seguro(expresion)
        print("Resultado:", salida)
    else:
        print("Expresión no válida: contiene caracteres prohibidos")

if __name__ == "__main__":
    iniciar()

