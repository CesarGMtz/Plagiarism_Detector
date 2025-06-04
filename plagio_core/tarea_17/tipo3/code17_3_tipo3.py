import matplotlib.pyplot as plt
import numpy as np
import math

def input_funcion():
    print("Este graficador utiliza math y numpy.")
    return input("Introduce una expresión válida (usa x): ")

def evaluar_lista(expr, x_values):
    resultados = []
    contexto = {"math": math, "np": np}
    for x in x_values:
        try:
            resultados.append(eval(expr, {**contexto, "x": x}))
        except:
            resultados.append(np.nan)
    return resultados

def preparar_y_mostrar(expr):
    x_vals = np.linspace(-10, 10, 600)
    y_vals = evaluar_lista(expr, x_vals)

    plt.plot(x_vals, y_vals, 'b-', label=expr)
    plt.title("Representación de función")
    plt.xlabel("x")
    plt.ylabel("Resultado")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    expresion = input_funcion()
    preparar_y_mostrar(expresion)

if __name__ == "__main__":
    main()

