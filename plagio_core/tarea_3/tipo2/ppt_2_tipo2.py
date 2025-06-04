import random

def pedir_jugada():
    return input("Selecciona (piedra / papel / tijera): ").lower()

def partida():
    vence = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}
    jugadas = list(vence.keys())

    humano = pedir_jugada()
    maquina = random.choice(jugadas)

    if humano not in jugadas:
        print("Opción inválida.")
        return

    print("Elegiste:", humano)
    print("Computadora:", maquina)

    if humano == maquina:
        print("Empate")
    elif vence[humano] == maquina:
        print("Ganaste")
    else:
        print("Derrota")

partida()

