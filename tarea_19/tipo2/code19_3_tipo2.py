import matplotlib.pyplot as plt
from collections import defaultdict
import string

def cargar_contenido(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return archivo.read()

def limpiar_y_contar(cadena):
    texto = cadena.lower()
    for simbolo in string.punctuation:
        texto = texto.replace(simbolo, "")
    lista = texto.split()
    contador = defaultdict(int)
    for palabra in lista:
        contador[palabra] += 1
    return contador

def obtener_principales(diccionario, n=10):
    return sorted(diccionario.items(), key=lambda par: par[1], reverse=True)[:n]

def dibujar_grafico(pares):
    etiquetas, valores = zip(*pares)
    plt.bar(etiquetas, valores)
    plt.title("Top palabras más usadas")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

data = cargar_contenido("texto.txt")
conteo = limpiar_y_contar(data)
principales = obtener_principales(conteo)
dibujar_grafico(principales)

