import random

def partida():
    jugadas = ['piedra', 'papel', 'tijera']
    puntos = {'jugador': 0, 'cpu': 0}

    for i in range(3):
        jugador = input("Tu jugada (piedra/papel/tijera): ").lower()
        cpu = random.choice(jugadas)

        if jugador not in jugadas:
            print("Entrada no válida.")
            continue

        print(f"CPU eligió: {cpu}")
        if jugador == cpu:
            print("Empate.")
        elif (jugador == 'piedra' and cpu == 'tijera') or \
             (jugador == 'papel' and cpu == 'piedra') or \
             (jugador == 'tijera' and cpu == 'papel'):
            puntos['jugador'] += 1
            print("Punto para ti.")
        else:
            puntos['cpu'] += 1
            print("Punto para la CPU.")

    print(f"Resultado final -> Tú: {puntos['jugador']} | CPU: {puntos['cpu']}")

partida()

