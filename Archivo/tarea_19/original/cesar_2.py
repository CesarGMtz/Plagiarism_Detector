import matplotlib.pyplot as plt
from collections import Counter
import string

def limpiar_texto(texto):
    texto = texto.lower()
    for simbolo in string.punctuation:
        texto = texto.replace(simbolo, "")
    return texto

def obtener_palabras_mas_comunes(texto, top_n=10):
    palabras = limpiar_texto(texto).split()
    contador = Counter(palabras)
    return contador.most_common(top_n)

def graficar_frecuencias(palabras_comunes):
    palabras, frecuencias = zip(*palabras_comunes)
    plt.bar(palabras, frecuencias)
    plt.xlabel("Palabras")
    plt.ylabel("Frecuencia")
    plt.title("Top 10 palabras más comunes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    with open("texto.txt", "r") as archivo:
        contenido = archivo.read()
    top10 = obtener_palabras_mas_comunes(contenido)
    graficar_frecuencias(top10)

