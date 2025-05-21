import matplotlib.pyplot as plt
import string

def cargar_texto(ruta):
    with open(ruta, "r") as f:
        return f.read().lower()

def limpiar(texto):
    return texto.translate(str.maketrans("", "", string.punctuation))

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def mostrar_top10(conteo):
    top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:10]
    claves, valores = zip(*top)
    plt.bar(claves, valores)
    plt.xticks(rotation=30)
    plt.title("10 Palabras más comunes")
    plt.tight_layout()
    plt.show()

texto = cargar_texto("texto.txt")
texto = limpiar(texto)
frecuencias = contar_palabras(texto)
mostrar_top10(frecuencias)

