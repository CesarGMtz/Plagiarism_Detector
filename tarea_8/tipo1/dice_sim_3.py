import random

def lanzar_dado():
    return random.randint(1, 6)

def simulacion(n):
    conteo = [0] * 6
    for _ in range(n):
        cara = lanzar_dado()
        conteo[cara - 1] += 1
    return conteo

def mostrar_tabla(resultados):
    print("\nHistograma de Lanzamientos:")
    for i, cantidad in enumerate(resultados):
        porcentaje = (cantidad / sum(resultados)) * 100
        print(f"{i + 1}: {cantidad:>3} → {'▇' * (cantidad // 5)} ({porcentaje:.1f}%)")

def jugar():
    veces = int(input("Lanzamientos: "))
    resultados = simulacion(veces)
    mostrar_tabla(resultados)

jugar()

