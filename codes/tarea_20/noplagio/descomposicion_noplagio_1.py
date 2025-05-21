import random

def crear_laberinto(w, h):
    maze = [[' ' for _ in range(w)] for _ in range(h)]

    def dividir(x, y, ancho, alto, orientacion):
        if ancho < 3 or alto < 3:
            return

        horizontal = orientacion == 'H'
        if horizontal:
            wy = y + random.randrange(2, alto - 1, 2)
            for i in range(x, x + ancho):
                maze[wy][i] = '#'
            puerta = x + random.randrange(1, ancho, 2)
            maze[wy][puerta] = ' '
            dividir(x, y, ancho, wy - y, 'V')
            dividir(x, wy + 1, ancho, y + alto - wy - 1, 'V')
        else:
            wx = x + random.randrange(2, ancho - 1, 2)
            for i in range(y, y + alto):
                maze[i][wx] = '#'
            puerta = y + random.randrange(1, alto, 2)
            maze[puerta][wx] = ' '
            dividir(x, y, wx - x, alto, 'H')
            dividir(wx + 1, y, x + ancho - wx - 1, alto, 'H')

    for i in range(w):
        maze[0][i] = maze[h-1][i] = '#'
    for i in range(h):
        maze[i][0] = maze[i][w-1] = '#'

    dividir(1, 1, w - 2, h - 2, 'H' if w < h else 'V')
    return maze

def mostrar(maze):
    for fila in maze:
        print(''.join(fila))

laberinto = crear_laberinto(21, 11)
mostrar(laberinto)

