import random

def generar_dados(n):
    return [random.randint(1, 6) for _ in range(n)]

def contar(valores):
    contador = [0]*6
    for v in valores:
        contador[v - 1] += 1
    return contador

def imprimir_histograma(valores):
    total = sum(valores)
    print("\nFrecuencia de caras con porcentaje:")
    for i, cantidad in enumerate(valores, 1):
        porcentaje = (cantidad / total) * 100
        simbolo = random.choice(['*', '■', '+'])
        print(f"{i}: {simbolo * (cantidad // 3)} ({porcentaje:.1f}%)")

def ejecutar():
    lanzamientos = generar_dados(90)
    conteo = contar(lanzamientos)
    imprimir_histograma(conteo)

ejecutar()

