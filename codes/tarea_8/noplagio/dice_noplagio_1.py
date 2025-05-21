import random

def lanzar():
    return [random.randint(1, 6) for _ in range(100)]

def contar(resultados):
    conteo = {i: resultados.count(i) for i in range(1, 7)}
    return conteo

def mostrar(conteo):
    print("\nDistribución horizontal:\n")
    for cara in range(1, 7):
        barra = f"{cara} → " + "-" * (conteo[cara] // 2)
        print(barra + f" ({conteo[cara]})")

def ejecutar():
    resultado = lanzar()
    conteo = contar(resultado)
    mostrar(conteo)

ejecutar()

