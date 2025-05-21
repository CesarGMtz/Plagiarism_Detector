import random

def simulacion(tiros):
    valores = [random.randint(1, 6) for _ in range(tiros)]
    return [valores.count(i) for i in range(1, 7)]

def generar_histograma(lista):
    print("\nHistograma de tiradas:")
    for i, val in enumerate(lista, 1):
        barra = '#' * (val // 2)
        print(f"Dado {i}: {barra} ({val})")

def main():
    intentos = int(input("Total de lanzamientos: "))
    frecuencia = simulacion(intentos)
    generar_histograma(frecuencia)

main()

