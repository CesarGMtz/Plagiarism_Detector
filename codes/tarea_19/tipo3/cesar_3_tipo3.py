import matplotlib.pyplot as plt
import string

def extraer_y_procesar(nombre):
    with open(nombre, encoding="utf-8") as f:
        contenido = f.read()
    contenido = contenido.lower()
    for c in string.punctuation:
        contenido = contenido.replace(c, "")
    return contenido.split()

def construir_frecuencia(lista):
    resultado = {}
    for elem in lista:
        resultado[elem] = resultado.get(elem, 0) + 1
    top = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    return top[:10]

def pintar(lista_top):
    etiquetas = []
    valores = []
    for par in lista_top:
        etiquetas.append(par[0])
        valores.append(par[1])
    fig = plt.figure()
    eje = fig.add_subplot(1,1,1)
    eje.bar(etiquetas, valores)
    eje.set_title("Top Palabras")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

palabras = extraer_y_procesar("texto.txt")
conteo = construir_frecuencia(palabras)
pintar(conteo)

