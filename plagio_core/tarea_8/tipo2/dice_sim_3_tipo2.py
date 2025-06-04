import random

def tirar_dado():
    return random.randint(1, 6)

def simular_tiros(repeticiones):
    registros = [0] * 6
    for _ in range(repeticiones):
        lado = tirar_dado()
        registros[lado - 1] += 1
    return registros

def imprimir_histograma(frecuencias):
    total = sum(frecuencias)
    print("\nResumen de lanzamientos:")
    for idx, cantidad in enumerate(frecuencias):
        porc = (cantidad / total) * 100
        barras = '█' * (cantidad // 5)
        print(f"{idx + 1}: {cantidad:>3} → {barras} ({porc:.1f}%)")

def iniciar():
    intentos = int(input("¿Cuántos lanzamientos? "))
    conteos = simular_tiros(intentos)
    imprimir_histograma(conteos)

iniciar()

