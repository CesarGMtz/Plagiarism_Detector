import random

def construir_laberinto(ancho, alto):
    laberinto = [['#'] * ancho for _ in range(alto)]
    pila = [(1, 1)]
    laberinto[1][1] = ' '

    while pila:
        cx, cy = pila[-1]
        opciones = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(opciones)
        movido = False

        for dx, dy in opciones:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx < ancho-1 and 1 <= ny < alto-1 and laberinto[ny][nx] == '#':
                laberinto[ny][nx] = ' '
                laberinto[cy + dy//2][cx + dx//2] = ' '
                pila.append((nx, ny))
                movido = True
                break
        if not movido:
            pila.pop()
    return laberinto

def mostrar_laberinto(laberinto):
    for fila in laberinto:
        print(''.join(fila))

lab = construir_laberinto(21, 11)
mostrar_laberinto(lab)

