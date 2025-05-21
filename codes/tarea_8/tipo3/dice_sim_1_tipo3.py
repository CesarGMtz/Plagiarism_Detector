import random
from collections import Counter

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_n_veces(n):
    return [lanzar_dado() for _ in range(n)]

def contar_resultados(tiradas):
    return Counter(tiradas)

def imprimir_resultados(contador):
    print("Frecuencia de cada cara:")
    for cara in range(1, 7):
        print(f"{cara}: {contador[cara]}")

def pedir_cantidad():
    try:
        return int(input("¿Cuántas veces deseas lanzar el dado? "))
    except ValueError:
        print("Entrada inválida.")
        return 0

def simulacion():
    while True:
        cantidad = pedir_cantidad()
        if cantidad <= 0:
            continue
        resultados = lanzar_n_veces(cantidad)
        conteo = contar_resultados(resultados)
        imprimir_resultados(conteo)
        if input("¿Salir? (s/n): ").lower() == "s":
            break

simulacion()

