import matplotlib.pyplot as plt
import re

def obtener_top10_palabras(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        texto = archivo.read().lower()
    palabras = re.findall(r'\b\w+\b', texto)
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    top10 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:10]
    return top10

def crear_bar_chart(palabras, cantidades):
    fig, ax = plt.subplots()
    ax.bar(palabras, cantidades)
    ax.set_ylabel("Ocurrencias")
    ax.set_title("Palabras más frecuentes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

pares = obtener_top10_palabras("texto.txt")
palabras, valores = zip(*pares)
crear_bar_chart(palabras, valores)

