import matplotlib.pyplot as plt
import numpy as np

class FuncionGraficador:
    def __init__(self):
        self.expresion = ""
        self.x = np.linspace(-10, 10, 400)
        self.y = []

    def pedir_funcion(self):
        print("Bienvenido al graficador tipo objeto.")
        self.expresion = input("Escribe una función de x: ")

    def calcular(self):
        for valor in self.x:
            try:
                resultado = eval(self.expresion)
            except:
                resultado = None
            self.y.append(resultado)

    def mostrar(self):
        plt.plot(self.x, self.y)
        plt.title("Gráfica generada")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

def ejecutar():
    app = FuncionGraficador()
    app.pedir_funcion()
    app.calcular()
    app.mostrar()

if __name__ == "__main__":
    ejecutar()

