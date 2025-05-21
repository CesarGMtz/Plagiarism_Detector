import random

def lanzar():
    return random.randint(1, 6)

def contar(n):
    resultado = [0] * 6
    for _ in range(n):
        r = lanzar()
        resultado[r - 1] += 1
    return resultado

def ver_histograma(frecuencias):
    total = sum(frecuencias)
    print("\nHistograma:")
    for i, val in enumerate(frecuencias):
        porcentaje = (val / total) * 100
        barras = '█' * (val // 5)
        print(f"{i+1}: {val} → {barras} ({porcentaje:.1f}%)")

def iniciar():
    n = int(input("Lanzamientos de dado: "))
    resultados = contar(n)
    ver_histograma(resultados)

iniciar()

