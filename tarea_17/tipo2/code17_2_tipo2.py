import matplotlib.pyplot as plt
import numpy as np

def visualizar(fx):
    x = np.linspace(-10, 10, 500)
    try:
        y = [eval(fx) for x in x]
        plt.plot(x, y)
        plt.title(f"Gráfica de f(x) = {fx}")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.grid(True)
        plt.show()
    except Exception as err:
        print("Error al graficar:", err)

def ejecutar():
    print("== Graficador de expresiones ==")
    formula = input("Ingresa una función con x (ej. x**2 + 3): ")
    visualizar(formula)

if __name__ == "__main__":
    ejecutar()

