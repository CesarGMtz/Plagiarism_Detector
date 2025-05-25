import random

def jugar_partida():
    elecciones = ['piedra', 'papel', 'tijera']
    eleccion_pc = random.choice(elecciones)
    eleccion_jugador = input("Tu jugada (piedra/papel/tijera): ").lower()

    if eleccion_jugador not in elecciones:
        print("¡Esa no es una opción válida!")
        return

    print("La computadora eligió:", eleccion_pc)

    if eleccion_jugador == eleccion_pc:
        print("Empate.")
    elif (eleccion_jugador == 'piedra' and eleccion_pc == 'tijera') or \
         (eleccion_jugador == 'papel' and eleccion_pc == 'piedra') or \
         (eleccion_jugador == 'tijera' and eleccion_pc == 'papel'):
        print("Ganaste.")
    else:
        print("Has perdido.")

jugar_partida()

