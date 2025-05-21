import random

class JuegoPPT:
    def __init__(self):
        self.opciones = ['piedra', 'papel', 'tijera']

    def elegir_cpu(self):
        return random.choice(self.opciones)

    def evaluar(self, jugador, cpu):
        if jugador == cpu:
            return "Empate"
        if (jugador == 'piedra' and cpu == 'tijera') or \
           (jugador == 'papel' and cpu == 'piedra') or \
           (jugador == 'tijera' and cpu == 'papel'):
            return "Ganaste"
        return "Perdiste"

    def jugar(self):
        jugada = input("Tu jugada: ").lower()
        if jugada not in self.opciones:
            print("Entrada no válida.")
            return
        cpu_jugada = self.elegir_cpu()
        print("CPU eligió:", cpu_jugada)
        print(self.evaluar(jugada, cpu_jugada))

JuegoPPT().jugar()

