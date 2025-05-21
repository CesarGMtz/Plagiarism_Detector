import matplotlib.pyplot as plt
from collections import defaultdict
import string

def texto_limpio(ruta):
    with open(ruta) as doc:
        datos = doc.read().lower()
    for signo in string.punctuation:
        datos = datos.replace(signo, "")
    return datos

def contar_palabras(lista):
    total = defaultdict(int)
    for palabra in lista:
        total[palabra] += 1
    return sorted(total.items(), key=lambda par: par[1], reverse=True)[:10]

def graficar_etiquetas(pares):
    plt.bar([k for k, _ in pares], [v for _, v in pares])
    plt.title("Frecuencia de palabras")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def iniciar():
    datos = texto_limpio("texto.txt")
    palabras = datos.split()
    top = contar_palabras(palabras)
    graficar_etiquetas(top)

iniciar()

