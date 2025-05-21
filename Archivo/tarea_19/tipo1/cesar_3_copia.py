import matplotlib.pyplot as plt
from collections import defaultdict
import string

def cargar(nombre_archivo):
    with open(nombre_archivo, encoding="utf-8") as archivo:
        return archivo.read()

def limpiar_texto(txt):
    txt = txt.lower()
    for signo in string.punctuation:
        txt = txt.replace(signo, "")
    lista = txt.split()
    conteo = defaultdict(int)
    for item in lista:
        conteo[item] += 1
    return conteo

def obtener_top10(diccionario):
    return sorted(diccionario.items(), key=lambda el: el[1], reverse=True)[:10]

def dibujar_grafico(info):
    etiquetas, numeros = zip(*info)
    plt.bar(etiquetas, numeros)
    plt.xticks(rotation=40)
    plt.title("Frecuencia")
    plt.tight_layout()
    plt.show()

contenido = cargar("texto.txt")
frecuencias = limpiar_texto(contenido)
palabras_top = obtener_top10(frecuencias)
dibujar_grafico(palabras_top)

