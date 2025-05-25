import re
import ast
import operator

ALLOWED_NAMES = {"abs": abs, "round": round}

def is_safe_expression(expr):
    allowed_chars = re.compile(r'^[0-9+\-*/()., \t\n]+$')
    return bool(allowed_chars.match(expr))

def safe_eval(expr):
    try:
        node = ast.parse(expr, mode='eval')
        for subnode in ast.walk(node):
            if isinstance(subnode, ast.Call):
                return "Error: No se permiten funciones"
            elif isinstance(subnode, ast.Name):
                if subnode.id not in ALLOWED_NAMES:
                    return "Error: Nombre no permitido"
        return eval(compile(node, '<string>', mode='eval'))
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    expr = input("Ingresa una expresión matemática: ")
    if is_safe_expression(expr):
        result = safe_eval(expr)
        print("Resultado:", result)
    else:
        print("Expresión inválida: caracteres no permitidos")

if __name__ == "__main__":
    main()

