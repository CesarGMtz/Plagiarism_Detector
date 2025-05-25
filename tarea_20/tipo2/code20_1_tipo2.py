import random

def generar_laberinto(ancho, alto):
    mapa = [["#"] * ancho for _ in range(alto)]
    pila = [(1, 1)]
    mapa[1][1] = " "

    while pila:
        cx, cy = pila[-1]
        movimientos = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(movimientos)
        avance = False

        for dx, dy in movimientos:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx < ancho - 1 and 1 <= ny < alto - 1 and mapa[ny][nx] == "#":
                mapa[ny][nx] = " "
                mapa[cy + dy // 2][cx + dx // 2] = " "
                pila.append((nx, ny))
                avance = True
                break

        if not avance:
            pila.pop()

    return mapa

def mostrar_laberinto(matriz):
    for fila in matriz:
        print("".join(fila))

laberinto = generar_laberinto(21, 11)
mostrar_laberinto(laberinto)

