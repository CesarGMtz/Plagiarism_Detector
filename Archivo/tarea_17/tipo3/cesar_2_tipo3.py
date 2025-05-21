import numpy as np
import matplotlib.pyplot as plt

def solicitar_expresion():
    return input("Ingresa una ecuación matemática (ej: x**3 - x): ")

def generar_rango(inicio=-10, fin=10, pasos=500):
    return np.linspace(inicio, fin, pasos)

def calcular_resultados(expresion, datos_x):
    resultados = []
    for x in datos_x:
        try:
            resultados.append(eval(expresion))
        except:
            resultados.append(None)
    return resultados

def construir_grafico(xs, ys, etiqueta):
    plt.figure(figsize=(8,5))
    plt.plot(xs, ys, linewidth=2)
    plt.title(f"Función: {etiqueta}")
    plt.xlabel("Valor de X")
    plt.ylabel("Valor de Y")
    plt.grid()
    plt.show()

def graficador_general():
    expr = solicitar_expresion()
    x_datos = generar_rango()
    y_datos = calcular_resultados(expr, x_datos)
    construir_grafico(x_datos, y_datos, expr)

if __name__ == "__main__":
    graficador_general()

