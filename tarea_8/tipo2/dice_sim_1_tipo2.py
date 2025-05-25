import random
from collections import Counter

def simular_dados(repeticiones):
    tiradas = [random.randint(1, 6) for _ in range(repeticiones)]
    return Counter(tiradas)

def imprimir_resultados(frecuencias):
    print("\nResumen de lanzamientos:")
    for cara in range(1, 7):
        total = frecuencias.get(cara, 0)
        print(f"{cara}: {'#' * total} ({total})")

def ejecutar():
    print("🎲 Lanzamiento de dado 🎲")
    try:
        veces = int(input("¿Cuántos lanzamientos deseas realizar? "))
        resultados = simular_dados(veces)
        imprimir_resultados(resultados)
    except:
        print("Entrada inválida.")

ejecutar()

