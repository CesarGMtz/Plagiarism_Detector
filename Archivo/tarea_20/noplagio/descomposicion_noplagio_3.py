import random
from collections import deque

def crear(ancho, alto):
    grid = [['#'] * ancho for _ in range(alto)]
    visitado = [[False] * ancho for _ in range(alto)]
    cola = deque([(1, 1)])
    grid[1][1] = ' '
    visitado[1][1] = True

    while cola:
        x, y = cola.popleft()
        for dx, dy in random.sample([(2, 0), (-2, 0), (0, 2), (0, -2)], 4):
            nx, ny = x + dx, y + dy
            if 1 <= nx < ancho-1 and 1 <= ny < alto-1 and not visitado[ny][nx]:
                grid[ny][nx] = ' '
                grid[y + dy//2][x + dx//2] = ' '
                visitado[ny][nx] = True
                cola.append((nx, ny))
    return grid

def ver(m):
    for fila in m:
        print(''.join(fila))

ver(crear(21, 11))

