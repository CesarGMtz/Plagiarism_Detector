import random

def obtener_carta():
    return random.randint(1, 11)

def turno_jugador():
    total = 0
    while True:
        carta = obtener_carta()
        total += carta
        print(f"Tu carta: {carta}, total: {total}")
        if total > 21:
            print("Te pasaste. Pierdes.")
            return total
        respuesta = input("¿Otra carta? (s/n): ").lower()
        if respuesta != 's':
            break
    return total

def turno_computadora():
    total = 0
    while total < 17:
        carta = obtener_carta()
        total += carta
        print(f"La computadora saca: {carta}, total: {total}")
    return total

def main():
    print("Blackjack contra la computadora")
    jugador = turno_jugador()
    if jugador > 21:
        return
    computadora = turno_computadora()
    if computadora > 21 or jugador > computadora:
        print("¡Ganaste!")
    elif jugador < computadora:
        print("Perdiste.")
    else:
        print("Empate.")

main()

