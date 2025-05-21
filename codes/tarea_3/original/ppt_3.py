import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    puntos_jugador = 0
    puntos_cpu = 0

    for _ in range(3):
        eleccion_cpu = random.choice(opciones)
        eleccion = input("Elige piedra, papel o tijera: ").lower()

        if eleccion not in opciones:
            print("Entrada no válida.")
            continue

        print(f"La computadora eligió: {eleccion_cpu}")
        if eleccion == eleccion_cpu:
            print("Empate.")
        elif (eleccion == 'piedra' and eleccion_cpu == 'tijera') or              (eleccion == 'papel' and eleccion_cpu == 'piedra') or              (eleccion == 'tijera' and eleccion_cpu == 'papel'):
            print("¡Punto para ti!")
            puntos_jugador += 1
        else:
            print("Punto para la computadora.")
            puntos_cpu += 1

    print(f"\nMarcador final - Tú: {puntos_jugador} | Computadora: {puntos_cpu}")

jugar()