import random

class Tablero:
    def __init__(self):
        self.grid = [[" "] * 3 for _ in range(3)]

    def dibujar(self):
        for fila in self.grid:
            print(" | ".join(fila))
            print("-----")

    def mover(self, fila, col, jugador):
        if self.grid[fila][col] == " ":
            self.grid[fila][col] = jugador
            return True
        return False

    def estado_ganador(self, p):
        g = self.grid
        return any(all(g[i][j] == p for j in range(3)) for i in range(3)) or \
               any(all(g[j][i] == p for j in range(3)) for i in range(3)) or \
               all(g[i][i] == p for i in range(3)) or all(g[i][2 - i] == p for i in range(3))

def simulacion():
    juego = Tablero()
    jugador = "X"
    total = 0
    while total < 9:
        r, c = random.randint(0, 2), random.randint(0, 2)
        if juego.mover(r, c, jugador):
            total += 1
            if juego.estado_ganador(jugador):
                juego.dibujar()
                print(f"{jugador} ha ganado (simulado)")
                return
            jugador = "O" if jugador == "X" else "X"
    juego.dibujar()
    print("Empate en simulación")

simulacion()

