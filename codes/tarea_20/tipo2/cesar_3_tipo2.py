import random

def configurar_laberinto(w, h):
    return [['#' for _ in range(w)] for _ in range(h)]

def dfs_laberinto(lab, origen):
    pila = [origen]
    w, h = len(lab[0]), len(lab)
    lab[origen[1]][origen[0]] = ' '

    while pila:
        actual = pila[-1]
        dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(dirs)
        expandido = False
        for dx, dy in dirs:
            nx, ny = actual[0] + dx, actual[1] + dy
            if 0 < nx < w and 0 < ny < h and lab[ny][nx] == '#':
                lab[ny][nx] = ' '
                lab[actual[1] + dy//2][actual[0] + dx//2] = ' '
                pila.append((nx, ny))
                expandido = True
                break
        if not expandido:
            pila.pop()

def mostrar_laberinto(lab):
    for r in lab:
        print(''.join(r))

def generar(ancho, alto):
    lab = configurar_laberinto(ancho, alto)
    dfs_laberinto(lab, (1, 1))
    return lab

laberinto = generar(21, 11)
mostrar_laberinto(laberinto)

