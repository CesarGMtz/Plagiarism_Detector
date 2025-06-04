import random

def obtener_eleccion():
    return input("Tu jugada (piedra, papel, tijera): ").lower()

def jugar():
    reglas = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}
    opciones = list(reglas.keys())

    jugador = obtener_eleccion()
    computadora = random.choice(opciones)

    if jugador not in opciones:
        print("Jugada inválida.")
        return

    print("Tú elegiste:", jugador)
    print("La computadora eligió:", computadora)

    if jugador == computadora:
        print("Empate.")
    elif reglas[jugador] == computadora:
        print("¡Ganaste!")
    else:
        print("Perdiste.")

jugar()