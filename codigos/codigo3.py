import statistics

def obtener_media(numeros):
    return sum(numeros) / len(numeros)

def obtener_mediana(numeros):
    return statistics.median(numeros)

def obtener_moda(numeros):
    return statistics.mode(numeros)

def obtener_desviacion(numeros):
    return statistics.stdev(numeros)

def imprimir_resultados(datos):
    print("Datos proporcionados:", datos)
    print("Media:", obtener_media(datos))
    print("Mediana:", obtener_mediana(datos))
    print("Moda:", obtener_moda(datos))
    print("Desviación estándar:", obtener_desviacion(datos))

def leer_entrada():
    valores = input("Escribe números separados por espacios: ")
    return [float(valor) for valor in valores.split()]

def iniciar():
    lista = leer_entrada()
    imprimir_resultados(lista)

if __name__ == "__main__":
    iniciar()

