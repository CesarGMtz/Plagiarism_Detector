import matplotlib.pyplot as plt
import numpy as np
import math

def evaluar_funcion(f_str, x_val):
    try:
        return eval(f_str, {"x": x_val, "np": np, "math": math})
    except:
        return None

def graficar():
    f_str = input("Ingresa una función en x: ")
    x = np.linspace(-10, 10, 500)
    y = []

    for val in x:
        result = evaluar_funcion(f_str, val)
        y.append(result)

    plt.plot(x, y)
    plt.title(f"Gráfico de: {f_str}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    graficar()

