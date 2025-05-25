import statistics

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_moda(lista):
    return statistics.mode(lista)

def calcular_desviacion(lista):
    return statistics.stdev(lista)

def mostrar_estadisticas(valores):
    print("Valores ingresados:", valores)
    print("Promedio:", calcular_promedio(valores))
    print("Mediana:", calcular_mediana(valores))
    print("Moda:", calcular_moda(valores))
    print("Desviación estándar:", calcular_desviacion(valores))

def obtener_numeros():
    entrada = input("Introduce números separados por espacio: ")
    return [float(x) for x in entrada.split()]

def main():
    datos = obtener_numeros()
    mostrar_estadisticas(datos)

if __name__ == "__main__":
    main()

