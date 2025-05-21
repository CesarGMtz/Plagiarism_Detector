import random

def lanzar_dados(n):
    return [random.randint(1, 6) for _ in range(n)]

def frecuencia(resultados):
    frec = [0]*6
    for r in resultados:
        frec[r - 1] += 1
    return frec

def histograma_vertical(frec):
    max_val = max(frec)
    print("\nHistograma vertical:")
    for nivel in range(max_val, 0, -1):
        linea = ""
        for valor in frec:
            linea += " * " if valor >= nivel else "   "
        print(linea)
    print(" 1  2  3  4  5  6")

def main():
    datos = lanzar_dados(60)
    conteo = frecuencia(datos)
    histograma_vertical(conteo)

main()

