class JuegoTresEnLinea:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugador = "X"
        self.movimientos = 0

    def mostrar(self):
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 5)

    def colocar(self, fila, col):
        if self.tablero[fila][col] == " ":
            self.tablero[fila][col] = self.jugador
            self.movimientos += 1
            return True
        return False

    def verificar(self):
        t = self.tablero
        j = self.jugador
        for i in range(3):
            if all(t[i][x] == j for x in range(3)) or all(t[x][i] == j for x in range(3)):
                return True
        if t[0][0] == t[1][1] == t[2][2] == j or t[0][2] == t[1][1] == t[2][0] == j:
            return True
        return False

    def cambiar_turno(self):
        self.jugador = "O" if self.jugador == "X" else "X"

    def jugar(self):
        while self.movimientos < 9:
            self.mostrar()
            try:
                f, c = map(int, input(f"{self.jugador}, juega (fila columna): ").split())
                if self.colocar(f, c):
                    if self.verificar():
                        self.mostrar()
                        print(f"{self.jugador} gana")
                        return
                    self.cambiar_turno()
                else:
                    print("Espacio ocupado.")
            except:
                print("Entrada inválida.")
        self.mostrar()
        print("Empate")

JuegoTresEnLinea().jugar()

