import random

def inicializar_laberinto(ancho, alto):
    return [['#'] * ancho for _ in range(alto)]

def mover(stack, lab, ancho, alto):
    x, y = stack[-1]
    dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 1 <= nx < ancho - 1 and 1 <= ny < alto - 1 and lab[ny][nx] == '#':
            lab[ny][nx] = ' '
            lab[y + dy//2][x + dx//2] = ' '
            stack.append((nx, ny))
            return True
    return False

def construir_laberinto(ancho, alto):
    lab = inicializar_laberinto(ancho, alto)
    pila = [(1, 1)]
    lab[1][1] = ' '
    while pila:
        if not mover(pila, lab, ancho, alto):
            pila.pop()
    return lab

def mostrar(lab):
    for fila in lab:
        print(''.join(fila))

maze = construir_laberinto(21, 11)
mostrar(maze)

