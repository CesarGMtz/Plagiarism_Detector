import matplotlib.pyplot as plt
import numpy as np

def graficar_funcion():
    print("== Visualizador de Funciones ==")
    expresion = input("Escribe una función de x (por ejemplo: x**2 - 4*x + 1): ")

    try:
        funcion = lambda x: eval(expresion)
        valores_x = np.linspace(-10, 10, 400)
        valores_y = [funcion(x) for x in valores_x]

        plt.plot(valores_x, valores_y, label=f"f(x) = {expresion}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Representación Gráfica")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as error:
        print("No se pudo graficar:", error)

if __name__ == "__main__":
    graficar_funcion()

