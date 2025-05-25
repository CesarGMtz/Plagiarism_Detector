import random
import numpy as np

def inicializar(ancho, alto):
    m = np.ones((alto, ancho), dtype=int)
    m[1::2,1::2] = 0
    return m

def conectar(matriz, x, y):
    dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 < nx < matriz.shape[1]-1 and 0 < ny < matriz.shape[0]-1 and matriz[ny][nx] == 1:
            matriz[ny][nx] = 0
            matriz[y + dy//2][x + dx//2] = 0
            conectar(matriz, nx, ny)

def mostrar(matriz):
    for fila in matriz:
        print(''.join(' ' if c == 0 else '#' for c in fila))

maze = inicializar(21, 11)
conectar(maze, 1, 1)
mostrar(maze)

