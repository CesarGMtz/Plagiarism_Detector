import random

def pedir_carta():
    return random.randint(1, 11)

def blackjack():
    jugador = 0
    computadora = 0
    seguir = 's'

    print("Bienvenido al Blackjack básico.")

    while seguir == 's':
        carta = pedir_carta()
        jugador += carta
        print(f"Tu carta: {carta} | Total: {jugador}")
        if jugador > 21:
            print("Te pasaste. Game Over.")
            return
        seguir = input("¿Quieres otra carta? (s/n): ")

    while computadora < 17:
        c = pedir_carta()
        computadora += c
        print(f"La computadora saca: {c} | Total: {computadora}")

    print("\n--- Resultado Final ---")
    print(f"Tú: {jugador} | Computadora: {computadora}")
    if computadora > 21 or jugador > computadora:
        print("Ganaste.")
    elif jugador < computadora:
        print("Perdiste.")
    else:
        print("Empate.")

blackjack()

