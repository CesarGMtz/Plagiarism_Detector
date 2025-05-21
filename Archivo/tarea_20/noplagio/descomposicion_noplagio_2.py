import random

def generar_laberinto(ancho, alto):
    lab = [['#' for _ in range(ancho)] for _ in range(alto)]
    for y in range(1, alto-1):
        for x in range(1, ancho-1):
            if (x + y) % 2 == 0:
                lab[y][x] = ' '
                if random.choice([True, False]):
                    lab[y][x+1] = ' '
                else:
                    lab[y+1][x] = ' '
    lab[1][1] = ' '
    lab[alto-2][ancho-2] = ' '
    return lab

def imprimir(lab):
    for fila in lab:
        print(''.join(fila))

maze = generar_laberinto(21, 11)
imprimir(maze)

