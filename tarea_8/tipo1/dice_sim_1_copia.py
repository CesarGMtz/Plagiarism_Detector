import random
from collections import Counter

def tirar_dados(num):
    tiradas = [random.randint(1, 6) for _ in range(num)]
    return Counter(tiradas)

def histograma(conteo):
    print("\nHistograma:")
    for num in range(1, 7):
        total = conteo.get(num, 0)
        print(f"{num}: {'*' * total} ({total})")

def ejecutar():
    print("Simulación de Dados")
    veces = int(input("Número de lanzamientos: "))
    conteo = tirar_dados(veces)
    histograma(conteo)

ejecutar()

