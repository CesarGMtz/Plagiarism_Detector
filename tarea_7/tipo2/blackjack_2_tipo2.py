import random

def sacar_carta():
    return random.randint(2, 11)

def turno(nombre):
    puntos = 0
    while puntos < 21:
        puntos += sacar_carta()
        print(f"{nombre} suma: {puntos}")
        if nombre == "Humano":
            seguir = input("¿Otra carta? (s/n): ").strip().lower()
            if seguir != 's':
                break
        else:
            if puntos >= 17:
                break
    return puntos

def resultado(j, c):
    print(f"\nMarcador → Tú: {j} | PC: {c}")
    if j > 21:
        print("Exceso de puntos. Pierdes.")
    elif c > 21 or j > c:
        print("¡Ganaste!")
    elif j < c:
        print("Derrota.")
    else:
        print("Empate.")

def jugar():
    print("== Bienvenido al Blackjack ==")
    puntos_jugador = turno("Humano")
    puntos_pc = turno("PC") if puntos_jugador <= 21 else 0
    resultado(puntos_jugador, puntos_pc)

jugar()

