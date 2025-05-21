import matplotlib.pyplot as plt
import numpy as np

def mostrar_grafica(expresion):
    x_vals = np.linspace(-10, 10, 500)
    try:
        y_vals = [eval(expresion) for x in x_vals]
        plt.plot(x_vals, y_vals)
        plt.title(f"Gráfica de: {expresion}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
    except Exception as error:
        print("Error al procesar la función:", error)

def principal():
    print("Este programa grafica funciones matemáticas.")
    expresion = input("Introduce la expresión de x: ")
    mostrar_grafica(expresion)

if __name__ == "__main__":
    principal()

