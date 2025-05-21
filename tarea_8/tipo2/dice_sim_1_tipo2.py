import random

def lanzar_dados(n):
    resultados = {i: 0 for i in range(1, 7)}
    for _ in range(n):
        cara = random.randint(1, 6)
        resultados[cara] += 1
    return resultados

def graficar(conteo):
    print("\nDistribución de Resultados:")
    for valor, rep in conteo.items():
        escala = rep // 5
        print(f"{valor}: {'=' * escala} ({rep})")

def principal():
    try:
        n = int(input("¿Cuántos lanzamientos de dado deseas hacer? "))
        resultados = lanzar_dados(n)
        graficar(resultados)
    except ValueError:
        print("Por favor, introduce un número entero válido.")

principal()

