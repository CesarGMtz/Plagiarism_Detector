import matplotlib.pyplot as plt
from collections import defaultdict
import string

def cargar_archivo(path):
    archivo = open(path, encoding="utf-8")
    texto = archivo.read()
    archivo.close()
    return texto

def limpiar_y_contar(texto):
    texto = texto.lower()
    for s in string.punctuation:
        texto = texto.replace(s, "")
    palabras = texto.split()
    conteo = defaultdict(int)
    for palabra in palabras:
        conteo[palabra] += 1
    return conteo

def generar_top10(dic):
    pares_ordenados = list(dic.items())
    pares_ordenados.sort(key=lambda x: x[1], reverse=True)
    return pares_ordenados[:10]

def dibujar(pares):
    etiquetas, cantidades = [], []
    for palabra, valor in pares:
        etiquetas.append(palabra)
        cantidades.append(valor)
    plt.bar(etiquetas, cantidades)
    plt.xticks(rotation=35)
    plt.title("Top 10 palabras frecuentes")
    plt.tight_layout()
    plt.show()

texto_base = cargar_archivo("texto.txt")
conteo = limpiar_y_contar(texto_base)
top10 = generar_top10(conteo)
dibujar(top10)

