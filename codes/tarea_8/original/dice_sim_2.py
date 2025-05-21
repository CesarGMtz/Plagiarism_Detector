import random

def simular(n):
    resultados = {i: 0 for i in range(1, 7)}
    for _ in range(n):
        d = random.randint(1, 6)
        resultados[d] += 1
    return resultados

def imprimir_histograma(datos):
    print("\nResultados:")
    for i in range(1, 7):
        barras = datos[i] // 10
        print(f"{i} → {'#' * barras} ({datos[i]})")

def inicio():
    intentos = int(input("Número de lanzamientos: "))
    resultados = simular(intentos)
    imprimir_histograma(resultados)

inicio()

