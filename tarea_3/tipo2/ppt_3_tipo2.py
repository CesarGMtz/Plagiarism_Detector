import random

def partida():
    jugadas = ['piedra', 'papel', 'tijera']
    score_humano = 0
    score_pc = 0

    for ronda in range(3):
        jugada_pc = random.choice(jugadas)
        jugada = input("Selecciona piedra, papel o tijera: ").lower()

        if jugada not in jugadas:
            print("Jugada inválida.")
            continue

        print(f"Computadora eligió: {jugada_pc}")

        if jugada == jugada_pc:
            print("Empate.")
        elif (jugada == 'piedra' and jugada_pc == 'tijera') or \
             (jugada == 'papel' and jugada_pc == 'piedra') or \
             (jugada == 'tijera' and jugada_pc == 'papel'):
            print("Ganas el punto.")
            score_humano += 1
        else:
            print("La computadora gana el punto.")
            score_pc += 1

    print(f"\nResultado final -> Tú: {score_humano} | PC: {score_pc}")

partida()

