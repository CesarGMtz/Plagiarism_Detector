import matplotlib.pyplot as plt
from collections import Counter
import string

def preprocesar(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    return texto.split()

def contar_frecuencias(lista_palabras):
    return Counter(lista_palabras).most_common(10)

def leer_texto(ruta):
    with open(ruta, "r") as f:
        return f.read()

def generar_grafica(datos):
    etiquetas = [x[0] for x in datos]
    cantidades = [x[1] for x in datos]
    plt.bar(etiquetas, cantidades)
    plt.xticks(rotation=45)
    plt.title("Top palabras frecuentes")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    texto = leer_texto("texto.txt")
    palabras = preprocesar(texto)
    top10 = contar_frecuencias(palabras)
    generar_grafica(top10)

