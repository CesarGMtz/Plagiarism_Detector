import random

def juego():
    opciones = ['piedra', 'papel', 'tijera']
    cpu = random.choice(opciones)
    usuario = input("Selecciona piedra, papel o tijera: ").lower()

    if usuario not in opciones:
        print("Opción inválida.")
        return

    print("La computadora eligió:", cpu)

    if usuario == cpu:
        print("Empate.")
    elif (usuario == 'piedra' and cpu == 'tijera') or \
         (usuario == 'papel' and cpu == 'piedra') or \
         (usuario == 'tijera' and cpu == 'papel'):
        print("Ganaste.")
    else:
        print("Perdiste.")

juego()

