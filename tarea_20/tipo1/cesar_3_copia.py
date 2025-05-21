import random

def iniciar_laberinto(ancho, alto):
    return [['#' for _ in range(ancho)] for _ in range(alto)]

def crear_laberinto(matriz, inicio):
    pila = [inicio]
    ancho, alto = len(matriz[0]), len(matriz)
    matriz[inicio[1]][inicio[0]] = ' '

    while pila:
        px, py = pila[-1]
        direcciones = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(direcciones)
        encontrado = False
        for dx, dy in direcciones:
            nx, ny = px + dx, py + dy
            if 0 < nx < ancho and 0 < ny < alto and matriz[ny][nx] == '#':
                matriz[ny][nx] = ' '
                matriz[py + dy//2][px + dx//2] = ' '
                pila.append((nx, ny))
                encontrado = True
                break
        if not encontrado:
            pila.pop()

def desplegar_laberinto(matriz):
    for fila in matriz:
        print(''.join(fila))

matriz = iniciar_laberinto(21, 11)
crear_laberinto(matriz, (1, 1))
desplegar_laberinto(matriz)

