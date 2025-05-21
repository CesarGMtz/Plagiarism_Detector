import matplotlib.pyplot as plt
import numpy as np
import math

def pedir_funcion():
    print("Graficación matemática")
    return input("Función matemática (usa x): ")

def calcular_valores(expr, x_vals):
    y_vals = []
    for x in x_vals:
        try:
            resultado = eval(expr, {"x": x, "math": math, "np": np})
        except:
            resultado = None
        y_vals.append(resultado)
    return y_vals

def mostrar_grafica(x_vals, y_vals, expr):
    plt.plot(x_vals, y_vals)
    plt.title(f"Gráfico de {expr}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

def main():
    expresion = pedir_funcion()
    x_data = np.linspace(-10, 10, 500)
    y_data = calcular_valores(expresion, x_data)
    mostrar_grafica(x_data, y_data, expresion)

if __name__ == "__main__":
    main()

