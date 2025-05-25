import matplotlib.pyplot as plt
from collections import Counter
import string

def procesar_texto(cadena):
    cadena = cadena.lower()
    for signo in string.punctuation:
        cadena = cadena.replace(signo, "")
    return cadena

def contar_palabras(texto, limite=10):
    lista = procesar_texto(texto).split()
    conteo = Counter(lista)
    return conteo.most_common(limite)

def mostrar_grafica(frecuencias):
    etiquetas, valores = zip(*frecuencias)
    plt.bar(etiquetas, valores)
    plt.xlabel("Palabras")
    plt.ylabel("Ocurrencias")
    plt.title("Frecuencia de palabras")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    with open("texto.txt", "r", encoding="utf-8") as f:
        datos = f.read()
    top = contar_palabras(datos)
    mostrar_grafica(top)

