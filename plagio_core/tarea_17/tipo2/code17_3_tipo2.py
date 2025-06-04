import matplotlib.pyplot as plt
import numpy as np
import math

def calcular_y(expr, x_valor):
    try:
        contexto = {"x": x_valor, "np": np, "math": math}
        return eval(expr, contexto)
    except:
        return None

def mostrar_grafica():
    expresion = input("Escribe una función en x: ")
    eje_x = np.linspace(-10, 10, 500)
    eje_y = [calcular_y(expresion, valor) for valor in eje_x]

    plt.plot(eje_x, eje_y)
    plt.title(f"Función: {expresion}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    mostrar_grafica()

