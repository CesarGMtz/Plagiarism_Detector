import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    gana_a = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}

    user = input("Tu jugada: ").strip().lower()
    pc = random.choice(opciones)

    print(f"Computadora: {pc}")

    if user == pc:
        print("Empate")
    elif user in gana_a and gana_a[user] == pc:
        print("Ganaste")
    elif user in opciones:
        print("Perdiste")
    else:
        print("Movimiento inválido.")

jugar()

