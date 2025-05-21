import matplotlib.pyplot as plt
import numpy as np

def ejecutar():
    print("Gráfica de función matemática")
    funcion_usuario = input("Escribe la función en x (por ejemplo: x**2 + x): ")

    try:
        funcion = lambda x: eval(funcion_usuario)
        valores_x = np.linspace(-10, 10, 400)
        valores_y = [funcion(x) for x in valores_x]

        plt.plot(valores_x, valores_y, label=f"f(x) = {funcion_usuario}")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Función graficada")
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as err:
        print("Ocurrió un error al graficar:", err)

if __name__ == "__main__":
    ejecutar()

