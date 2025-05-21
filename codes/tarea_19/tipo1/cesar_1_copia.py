import matplotlib.pyplot as plt
from collections import Counter
import string

def limpiar(cadena):
    cadena = cadena.lower()
    for c in string.punctuation:
        cadena = cadena.replace(c, "")
    return cadena

def top_palabras(cadena, n=10):
    lista = limpiar(cadena).split()
    conteo = Counter(lista)
    return conteo.most_common(n)

def graficar(palabras):
    etiquetas, valores = zip(*palabras)
    plt.bar(etiquetas, valores)
    plt.xlabel("Palabras")
    plt.ylabel("Cantidad")
    plt.title("Top 10 palabras")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    archivo = open("texto.txt", "r")
    texto = archivo.read()
    archivo.close()
    top = top_palabras(texto)
    graficar(top)

