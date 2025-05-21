import random

def generar_laberinto(ancho, alto):
    matriz = [[' ' for _ in range(ancho)] for _ in range(alto)]
    for j in range(alto):
        for i in range(ancho):
            if i % 2 == 0 or j % 2 == 0:
                matriz[j][i] = '#'

    for j in range(1, alto, 2):
        for i in range(1, ancho, 2):
            mov = random.choice([(0, -1), (1, 0)])
            dx, dy = mov
            if 0 <= i + dx < ancho and 0 <= j + dy < alto:
                matriz[j + dy][i + dx] = ' '

    return matriz

def imprimir_laberinto(matriz):
    for fila in matriz:
        print(''.join(fila))

resultado = generar_laberinto(21, 11)
imprimir_laberinto(resultado)

