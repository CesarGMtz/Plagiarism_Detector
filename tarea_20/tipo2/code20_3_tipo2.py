import random

def crear_mapa(ancho, alto):
    return [["#" for _ in range(ancho)] for _ in range(alto)]

def laberinto_backtrack(mapa, inicio):
    pila = [inicio]
    ancho, alto = len(mapa[0]), len(mapa)
    mapa[inicio[1]][inicio[0]] = " "

    while pila:
        cx, cy = pila[-1]
        direcciones = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(direcciones)
        extendido = False

        for dx, dy in direcciones:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < ancho and 0 < ny < alto and mapa[ny][nx] == "#":
                mapa[ny][nx] = " "
                mapa[cy + dy // 2][cx + dx // 2] = " "
                pila.append((nx, ny))
                extendido = True
                break

        if not extendido:
            pila.pop()

def mostrar_mapa(matriz):
    for fila in matriz:
        print("".join(fila))

estructura = crear_mapa(21, 11)
laberinto_backtrack(estructura, (1, 1))
mostrar_mapa(estructura)

