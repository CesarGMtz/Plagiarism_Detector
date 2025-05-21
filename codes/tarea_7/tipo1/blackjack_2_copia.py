import random

def obtener():
    return random.choice(range(2, 12))

def turno(nombre):
    total = 0
    while total < 21:
        total += obtener()
        print(f"{nombre} lleva: {total}")
        if nombre == "Jugador":
            op = input("¿Otra carta? (s/n): ").strip().lower()
            if op != 's':
                break
        else:
            if total >= 17:
                break
    return total

def decidir(j, c):
    print(f"\nPuntos finales → Tú: {j} | PC: {c}")
    if j > 21:
        print("¡Te pasaste!")
    elif c > 21 or j > c:
        print("¡Victoria!")
    elif j < c:
        print("Derrota.")
    else:
        print("Empate.")

def comenzar():
    print("Bienvenido a Blackjack vs PC")
    jugador = turno("Jugador")
    pc = 0 if jugador > 21 else turno("PC")
    decidir(jugador, pc)

comenzar()

