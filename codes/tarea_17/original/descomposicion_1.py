import matplotlib.pyplot as plt
import numpy as np

def graficar_funcion(expr):
    x = np.linspace(-10, 10, 500)
    try:
        y = [eval(expr) for x in x]
        plt.plot(x, y)
        plt.title(f"f(x) = {expr}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.show()
    except Exception as e:
        print("No se pudo graficar la función:", e)

def main():
    print("Bienvenido al graficador de funciones.")
    expr = input("Introduce una función de x (ej. sin(x), x**3 - x): ")
    graficar_funcion(expr)

if __name__ == "__main__":
    main()

