import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.total = 0

    def tomar_turno(self, es_humano=False):
        while True:
            carta = random.randint(1, 11)
            self.total += carta
            print(f"{self.nombre} obtiene: {carta} → Total: {self.total}")
            if self.total > 21:
                print(f"{self.nombre} se pasó.")
                break
            if es_humano:
                r = input("¿Otra carta? (s/n): ").lower()
                if r != 's':
                    break
            else:
                if self.total >= 17:
                    break

def juego():
    print("=== Blackjack OO ===")
    jugador = Jugador("Jugador")
    computadora = Jugador("Computadora")
    
    jugador.tomar_turno(es_humano=True)
    if jugador.total <= 21:
        computadora.tomar_turno()

    print("\nResultado:")
    print(f"{jugador.nombre}: {jugador.total} | {computadora.nombre}: {computadora.total}")
    if jugador.total > 21:
        print("Perdiste.")
    elif computadora.total > 21 or jugador.total > computadora.total:
        print("Ganaste.")
    elif jugador.total < computadora.total:
        print("Perdiste.")
    else:
        print("Empate.")

juego()

