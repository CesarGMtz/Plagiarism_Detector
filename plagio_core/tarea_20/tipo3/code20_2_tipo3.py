import random

class Generador:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.laberinto = { (x, y): '#' for y in range(rows) for x in range(cols) }
        self._crear()

    def _crear(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if x % 2 != 0 and y % 2 != 0:
                    self.laberinto[(x, y)] = ' '
                    direcciones = [(1, 0), (0, -1)]
                    dx, dy = random.choice(direcciones)
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.cols and 0 <= ny < self.rows:
                        self.laberinto[(nx, ny)] = ' '

    def imprimir(self):
        for y in range(self.rows):
            print(''.join(self.laberinto[(x, y)] for x in range(self.cols)))

g = Generador(21, 11)
g.imprimir()

