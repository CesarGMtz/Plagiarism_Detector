import matplotlib.pyplot as plt
import numpy as np
import math

def calcular_valor(expr, x):
    try:
        return eval(expr, {"x": x, "np": np, "math": math})
    except:
        return None

def graficar_funcion():
    expresion = input("Función en x: ")
    puntos_x = np.linspace(-10, 10, 500)
    puntos_y = []

    for x in puntos_x:
        puntos_y.append(calcular_valor(expresion, x))

    plt.plot(puntos_x, puntos_y)
    plt.title("Función: " + expresion)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    graficar_funcion()

