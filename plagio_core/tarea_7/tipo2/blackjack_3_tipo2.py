import random

class Participante:
    def __init__(self, id_nombre):
        self.id_nombre = id_nombre
        self.puntos = 0

    def jugar_turno(self, humano=False):
        while True:
            nueva_carta = random.randint(1, 11)
            self.puntos += nueva_carta
            print(f"{self.id_nombre} recibe: {nueva_carta} → Total: {self.puntos}")

            if self.puntos > 21:
                print(f"{self.id_nombre} ha perdido por pasarse.")
                break

            if humano:
                respuesta = input("¿Deseas otra carta? (s/n): ").lower()
                if respuesta != 's':
                    break
            else:
                if self.puntos >= 17:
                    break

def comenzar_partida():
    print("== Blackjack con Clases ==")
    usuario = Participante("Humano")
    maquina = Participante("Máquina")

    usuario.jugar_turno(humano=True)
    if usuario.puntos <= 21:
        maquina.jugar_turno()

    print("\nResultado final:")
    print(f"{usuario.id_nombre}: {usuario.puntos} | {maquina.id_nombre}: {maquina.puntos}")

    if usuario.puntos > 21:
        print("Has perdido.")
    elif maquina.puntos > 21 or usuario.puntos > maquina.puntos:
        print("¡Ganaste!")
    elif usuario.puntos < maquina.puntos:
        print("Perdiste.")
    else:
        print("Empate.")

comenzar_partida()

