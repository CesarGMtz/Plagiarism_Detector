import numpy as np
import matplotlib.pyplot as plt

def procesar_entrada():
    return input("Ingresa la función de x a graficar: ")

def construir_y(x_vals, funcion):
    return [eval(funcion) for x in x_vals]

def dibujar_grafico(x_vals, y_vals, f_expr):
    plt.figure()
    plt.plot(x_vals, y_vals)
    plt.title("f(x) = " + f_expr)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True)
    plt.show()

def programa():
    funcion = procesar_entrada()
    x = np.linspace(-10, 10, 500)
    try:
        y = construir_y(x, funcion)
        dibujar_grafico(x, y, funcion)
    except:
        print("Error al intentar graficar")

if __name__ == "__main__":
    programa()

