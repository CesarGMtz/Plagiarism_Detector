import matplotlib.pyplot as plt
import collections
import string

def contar_palabras(archivo):
    with open(archivo, "r") as f:
        texto = f.read().translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = texto.split()
    return collections.Counter(palabras).most_common(10)

def mostrar(pares):
    nombres = [p[0] for p in pares]
    frecs = [p[1] for p in pares]
    plt.figure()
    plt.barh(nombres[::-1], frecs[::-1])  # horizontal y de abajo hacia arriba
    plt.xlabel("Frecuencia")
    plt.title("10 palabras más repetidas")
    plt.tight_layout()
    plt.show()

frecuencia = contar_palabras("texto.txt")
mostrar(frecuencia)

