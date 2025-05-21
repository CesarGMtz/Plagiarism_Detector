import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.total = 0

    def pedir_carta(self):
        nueva = random.randint(1, 11)
        self.total += nueva
        print(f"{self.nombre} saca un {nueva}. Total: {self.total}")

    def jugar(self, modo_manual=True):
        while self.total < 21:
            self.pedir_carta()
            if self.total >= 21:
                break
            if modo_manual and input("¿Deseas otra carta? (s/n): ").lower() != 's':
                break

def resultado(j1, j2):
    if j1.total > 21:
        return f"{j2.nombre} gana."
    elif j2.total > 21 or j1.total > j2.total:
        return f"{j1.nombre} gana."
    elif j1.total == j2.total:
        return "Empate."
    else:
        return f"{j2.nombre} gana."

def ejecutar_juego():
    jugador = Jugador("Jugador")
    maquina = Jugador("Máquina")

    jugador.jugar(modo_manual=True)
    maquina.jugar(modo_manual=False)

    print(resultado(jugador, maquina))

ejecutar_juego()

