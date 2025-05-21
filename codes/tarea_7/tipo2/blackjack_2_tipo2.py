import random

def carta_aleatoria():
    return random.randint(2, 11)

def turno_humano():
    total = 0
    while True:
        total += carta_aleatoria()
        print(f"Jugador tiene: {total}")
        if total > 21:
            print("¡Perdiste por pasarte!")
            break
        r = input("¿Otra carta? (s/n): ").lower()
        if r != 's':
            break
    return total

def turno_pc():
    total = 0
    while total < 17:
        total += carta_aleatoria()
        print(f"Computadora suma: {total}")
    return total

def juego():
    print("♠ Mini Blackjack ♠")
    puntos_jugador = turno_humano()
    if puntos_jugador <= 21:
        puntos_pc = turno_pc()
    else:
        puntos_pc = 0

    print(f"\nJugador: {puntos_jugador} | Computadora: {puntos_pc}")
    if puntos_jugador > 21:
        print("Derrota.")
    elif puntos_pc > 21 or puntos_jugador > puntos_pc:
        print("Victoria.")
    elif puntos_jugador < puntos_pc:
        print("Derrota.")
    else:
        print("Empate.")

juego()

