import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Graficador de funciones matemáticas")
    funcion_str = input("Ingresa una función en términos de x (ej. x**2 + 3*x): ")

    try:
        f = lambda x: eval(funcion_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [f(x) for x in x_vals]

        plt.plot(x_vals, y_vals, label=f"f(x) = {funcion_str}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Gráfica de la función")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print("Error al evaluar la función:", e)

if __name__ == "__main__":
    main()

