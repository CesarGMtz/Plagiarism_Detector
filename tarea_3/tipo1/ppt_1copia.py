import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    jugador = input("Elige piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("Opción inválida.")
        return

    print(f"Computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == 'piedra' and computadora == 'tijera') or          (jugador == 'papel' and computadora == 'piedra') or          (jugador == 'tijera' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

jugar()