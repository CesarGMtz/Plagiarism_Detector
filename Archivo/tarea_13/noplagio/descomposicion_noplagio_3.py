from sympy import sympify
from sympy.core.sympify import SympifyError

def evaluar_seguro(exp):
    try:
        resultado = sympify(exp, evaluate=True)
        return resultado
    except SympifyError:
        return "Expresión inválida"

def main():
    while True:
        exp = input("Expresión (o salir): ")
        if exp.strip().lower() == "salir":
            break
        print("Resultado:", evaluar_seguro(exp))

main()

