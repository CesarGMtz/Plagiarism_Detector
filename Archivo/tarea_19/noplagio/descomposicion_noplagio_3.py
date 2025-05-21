import matplotlib.pyplot as plt
import string

def limpiar_y_dividir(cadena):
    simbolos = str.maketrans("", "", string.punctuation)
    return cadena.translate(simbolos).lower().split()

def contar(palabras):
    resultado = {}
    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1
    return sorted(resultado.items(), key=lambda x: x[1], reverse=True)[:10]

def graficar(lista):
    etiquetas = [x[0] for x in lista]
    valores = [x[1] for x in lista]
    plt.bar(etiquetas, valores)
    plt.title("Top palabras")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.show()

with open("texto.txt") as archivo:
    contenido = archivo.read()
palabras = limpiar_y_dividir(contenido)
top = contar(palabras)
graficar(top)

