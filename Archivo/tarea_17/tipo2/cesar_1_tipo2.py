import numpy as np
import matplotlib.pyplot as plt

def obtener_datos():
    print("Generador de gráficas")
    return input("Escribe una función (ejemplo: x**2 - 4*x): ")

def generar_puntos(expr):
    f = lambda x: eval(expr)
    x = np.linspace(-10, 10, 400)
    y = []
    for val in x:
        y.append(f(val))
    return x, y

def graficar(x, y, expresion):
    plt.plot(x, y, label="f(x) = " + expresion)
    plt.title("Representación gráfica")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    expresion = obtener_datos()
    try:
        x, y = generar_puntos(expresion)
        graficar(x, y, expresion)
    except Exception as e:
        print("No se pudo generar la gráfica:", e)

if __name__ == "__main__":
    main()

