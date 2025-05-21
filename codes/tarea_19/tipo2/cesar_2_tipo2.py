import matplotlib.pyplot as plt
import string

def preparar_texto(texto):
    texto = texto.lower()
    for simbolo in string.punctuation:
        texto = texto.replace(simbolo, "")
    return texto.split()

def obtener_frecuencia(palabras):
    dic = {}
    for w in palabras:
        dic[w] = dic.get(w, 0) + 1
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)

def mostrar_grafica(pares):
    palabras, frec = [], []
    for p, f in pares[:10]:
        palabras.append(p)
        frec.append(f)
    plt.bar(palabras, frec)
    plt.xticks(rotation=25)
    plt.title("Palabras más usadas")
    plt.tight_layout()
    plt.show()

def abrir_archivo(nombre):
    with open(nombre, "r") as archivo:
        return archivo.read()

contenido = abrir_archivo("texto.txt")
tokens = preparar_texto(contenido)
resultados = obtener_frecuencia(tokens)
mostrar_grafica(resultados)

