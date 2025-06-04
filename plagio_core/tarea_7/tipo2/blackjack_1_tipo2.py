import random

def carta_aleatoria():
    return random.randint(1, 11)

def turno_humano():
    suma = 0
    while True:
        nueva = carta_aleatoria()
        suma += nueva
        print(f"Carta recibida: {nueva}, total actual: {suma}")
        if suma > 21:
            print("Te has pasado. Derrota.")
            return suma
        seguir = input("¿Deseas otra carta? (s/n): ").lower()
        if seguir != 's':
            break
    return suma

def turno_pc():
    suma = 0
    while suma < 17:
        nueva = carta_aleatoria()
        suma += nueva
        print(f"PC saca: {nueva}, suma total: {suma}")
    return suma

def ejecutar_juego():
    print("=== Blackjack VS Computadora ===")
    jugador = turno_humano()
    if jugador > 21:
        return
    pc = turno_pc()
    if pc > 21 or jugador > pc:
        print("¡Victoria!")
    elif jugador < pc:
        print("Derrota.")
    else:
        print("Empate.")

ejecutar_juego()

