import matplotlib.pyplot as plt
import numpy as np

def obtener_funcion():
    print("Puedes usar funciones como: x**2, np.sin(x), np.exp(x)")
    return input("Escribe la expresión de tu función: ")

def generar_funcion(code):
    def f(x):
        try:
            return eval(code)
        except:
            return np.nan
    return f

def main():
    expr = obtener_funcion()
    funcion = generar_funcion(expr)
    x = np.linspace(-10, 10, 400)
    y = [funcion(xi) for xi in x]

    plt.plot(x, y)
    plt.title("Resultado de la función ingresada")
    plt.xlabel("X")
    plt.ylabel("f(X)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

