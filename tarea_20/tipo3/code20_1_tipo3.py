import random

class Laberinto:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.grid = [['#'] * ancho for _ in range(alto)]
        self.generar(1, 1)

    def generar(self, x, y):
        self.grid[y][x] = ' '
        pasos = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(pasos)
        for dx, dy in pasos:
            nx, ny = x + dx, y + dy
            if 1 <= nx < self.ancho - 1 and 1 <= ny < self.alto - 1 and self.grid[ny][nx] == '#':
                self.grid[y + dy//2][x + dx//2] = ' '
                self.generar(nx, ny)

    def mostrar(self):
        for fila in self.grid:
            print(''.join(fila))

lab = Laberinto(21, 11)
lab.mostrar()

