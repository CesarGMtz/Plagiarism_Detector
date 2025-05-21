import matplotlib.pyplot as plt
from collections import defaultdict
import string

def leer_archivo(nombre):
    with open(nombre, encoding="utf-8") as f:
        return f.read()

def procesar(texto):
    texto = texto.lower()
    for c in string.punctuation:
        texto = texto.replace(c, "")
    palabras = texto.split()
    frecuencia = defaultdict(int)
    for palabra in palabras:
        frecuencia[palabra] += 1
    return frecuencia

def top_10_mas_frecuentes(frecuencia):
    return sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:10]

def graficar(datos):
    etiquetas, valores = zip(*datos)
    plt.bar(etiquetas, valores)
    plt.xticks(rotation=40)
    plt.title("Frecuencia de Palabras")
    plt.tight_layout()
    plt.show()

texto = leer_archivo("texto.txt")
conteo = procesar(texto)
top10 = top_10_mas_frecuentes(conteo)
graficar(top10)

