import ast
import re

class ValidadorExpresion:
    def __init__(self, expresion):
        self.expresion = expresion.strip()

    def contiene_solo_simbolos_validos(self):
        return bool(re.fullmatch(r'[0-9+\-*/().,\s]+', self.expresion))

    def tiene_estructuras_peligrosas(self):
        try:
            arbol = ast.parse(self.expresion, mode='eval')
            for nodo in ast.walk(arbol):
                if isinstance(nodo, (ast.Call, ast.Name)):
                    return True
            return False
        except:
            return True

    def evaluar(self):
        try:
            return eval(compile(ast.parse(self.expresion, mode='eval'), '', 'eval'))
        except Exception as e:
            return f"Error de ejecución: {e}"

def main():
    entrada = input("Expresión matemática: ")
    validador = ValidadorExpresion(entrada)

    if not validador.contiene_solo_simbolos_validos():
        print("Caracteres no permitidos.")
    elif validador.tiene_estructuras_peligrosas():
        print("Expresión potencialmente peligrosa.")
    else:
        print("Resultado:", validador.evaluar())

main()

