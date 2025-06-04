import matplotlib.pyplot as plt
import string

def leer_archivo(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read().lower()

def quitar_signos(cadena):
    return cadena.translate(str.maketrans("", "", string.punctuation))

def frecuencia_palabras(cadena):
    palabras = cadena.split()
    resumen = {}
    for palabra in palabras:
        resumen[palabra] = resumen.get(palabra, 0) + 1
    return resumen

def dibujar_top10(diccionario):
    top10 = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)[:10]
    etiquetas, cantidades = zip(*top10)
    plt.bar(etiquetas, cantidades)
    plt.xticks(rotation=30)
    plt.title("Palabras más frecuentes (Top 10)")
    plt.tight_layout()
    plt.show()

texto = leer_archivo("texto.txt")
texto = quitar_signos(texto)
conteo = frecuencia_palabras(texto)
dibujar_top10(conteo)

