import random

def menu_blackjack():
    print("🂡 Bienvenido al Blackjack 🂡")
    jugador = []
    computadora = []
    while True:
        jugador.append(random.randint(2, 11))
        print("Tus cartas:", jugador, "→ Total:", sum(jugador))
        if sum(jugador) > 21:
            print("Te pasaste. Has perdido.")
            return
        cont = input("¿Tomar otra carta? (s/n): ").strip().lower()
        if cont != 's':
            break
    while sum(computadora) < 17:
        computadora.append(random.randint(2, 11))
    print("Cartas de la computadora:", computadora, "→ Total:", sum(computadora))

    if sum(computadora) > 21 or sum(jugador) > sum(computadora):
        print("¡Ganaste!")
    elif sum(jugador) < sum(computadora):
        print("La computadora gana.")
    else:
        print("Empate.")

menu_blackjack()

