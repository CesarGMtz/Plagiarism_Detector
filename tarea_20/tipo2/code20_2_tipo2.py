import random

def construir_laberinto(ancho, alto):
    plano = [[' ' for _ in range(ancho)] for _ in range(alto)]

    for fila in range(alto):
        for col in range(ancho):
            if fila % 2 == 0 or col % 2 == 0:
                plano[fila][col] = "#"

    for fila in range(1, alto, 2):
        for col in range(1, ancho, 2):
            direccion = random.choice([(0, -1), (1, 0)])  # arriba o derecha
            dx, dy = direccion
            nx, ny = col + dx, fila + dy
            if 0 <= nx < ancho and 0 <= ny < alto:
                plano[ny][nx] = " "

    return plano

def mostrar(plano):
    for linea in plano:
        print("".join(linea))

lab = construir_laberinto(21, 11)
mostrar(lab)

