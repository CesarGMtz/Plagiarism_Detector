import random

def simular_dados(lanzamientos):
    resultados = {i: 0 for i in range(1, 7)}
    for _ in range(lanzamientos):
        cara = random.randint(1, 6)
        resultados[cara] += 1
    return resultados

def mostrar_histograma(valores):
    print("\nFrecuencia:")
    for cara in range(1, 7):
        barra = "#" * (valores[cara] // 10)
        print(f"{cara}: {barra} ({valores[cara]})")

def main():
    intentos = int(input("¿Cuántas veces lanzar el dado?: "))
    conteo = simular_dados(intentos)
    mostrar_histograma(conteo)

main()

