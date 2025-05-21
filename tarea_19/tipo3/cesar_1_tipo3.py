import string
import matplotlib.pyplot as plt

def analizar_frecuencias(entrada):
    conteo = {}
    entrada = entrada.lower()
    for simbolo in string.punctuation:
        entrada = entrada.replace(simbolo, " ")
    for palabra in entrada.split():
        if palabra not in conteo:
            conteo[palabra] = 1
        else:
            conteo[palabra] += 1
    lista = sorted(conteo.items(), key=lambda x: -x[1])
    return lista[:10]

def visualizar(etiquetas, valores):
    fig, eje = plt.subplots()
    eje.bar(etiquetas, valores)
    eje.set_title("Análisis de texto: palabras comunes")
    eje.set_xticklabels(etiquetas, rotation=40)
    plt.tight_layout()
    plt.show()

def procesar_archivo(nombre_archivo):
    with open(nombre_archivo) as f:
        texto = f.read()
    datos = analizar_frecuencias(texto)
    palabras = [x[0] for x in datos]
    repeticiones = [x[1] for x in datos]
    visualizar(palabras, repeticiones)

procesar_archivo("texto.txt")

