import random

def crear_base(ancho, alto):
    lab = [[' ' for _ in range(ancho)] for _ in range(alto)]
    for y in range(alto):
        for x in range(ancho):
            if x % 2 == 0 or y % 2 == 0:
                lab[y][x] = '#'
    return lab

def abrir_paredes(lab, ancho, alto):
    for y in range(1, alto, 2):
        for x in range(1, ancho, 2):
            dx, dy = random.choice([(0, -1), (1, 0)])
            nx, ny = x + dx, y + dy
            if 0 <= nx < ancho and 0 <= ny < alto:
                lab[ny][nx] = ' '

def generar_laberinto(ancho, alto):
    lab = crear_base(ancho, alto)
    abrir_paredes(lab, ancho, alto)
    return lab

def imprimir(lab):
    for fila in lab:
        print(''.join(fila))

laberinto = generar_laberinto(21, 11)
imprimir(laberinto)

