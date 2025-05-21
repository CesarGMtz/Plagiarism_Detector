import random

def jugar_blackjack():
    print("🂫 Blackjack Básico 🂫")
    puntos_j = 0
    terminado = False

    while not terminado:
        carta = random.randint(1, 11)
        puntos_j += carta
        print(f"Obtuviste {carta} → Total: {puntos_j}")
        if puntos_j > 21:
            print("Te pasaste. Fin.")
            return
        resp = input("¿Otra carta? (s/n): ").lower()
        if resp != 's':
            terminado = True

    puntos_c = 0
    while puntos_c < 17:
        puntos_c += random.randint(1, 11)

    print(f"\nJugador: {puntos_j} | Computadora: {puntos_c}")
    if puntos_c > 21 or puntos_j > puntos_c:
        print("Ganaste.")
    elif puntos_j < puntos_c:
        print("Perdiste.")
    else:
        print("Empate.")

jugar_blackjack()

