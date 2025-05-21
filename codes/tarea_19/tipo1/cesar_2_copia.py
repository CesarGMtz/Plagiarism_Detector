import matplotlib.pyplot as plt
import string

def leer_texto(path):
    f = open(path, "r")
    datos = f.read().lower()
    f.close()
    return datos

def eliminar_puntuacion(texto):
    return texto.translate(str.maketrans('', '', string.punctuation))

def contar(texto):
    palabras = texto.split()
    resultado = {}
    for p in palabras:
        if p in resultado:
            resultado[p] += 1
        else:
            resultado[p] = 1
    return resultado

def graficar_top10(dic):
    ordenado = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:10]
    keys, vals = zip(*ordenado)
    plt.bar(keys, vals)
    plt.xticks(rotation=30)
    plt.title("Top 10 Palabras")
    plt.tight_layout()
    plt.show()

data = leer_texto("texto.txt")
limpio = eliminar_puntuacion(data)
conteo = contar(limpio)
graficar_top10(conteo)

