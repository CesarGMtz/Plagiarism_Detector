import random

def entrada():
    return input("Tu elección (piedra, papel o tijera): ").lower()

def principal():
    gana_a = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}
    opciones = list(gana_a.keys())

    jugador = entrada()
    compu = random.choice(opciones)

    if jugador not in opciones:
        print("Entrada incorrecta.")
        return

    print("Elegiste:", jugador)
    print("Computadora eligió:", compu)

    if jugador == compu:
        print("Empate")
    elif gana_a[jugador] == compu:
        print("Tú ganas")
    else:
        print("Pierdes")

principal()

