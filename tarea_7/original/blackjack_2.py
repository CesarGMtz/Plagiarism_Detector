import random

def carta():
    return random.choice(range(2, 12))

def jugar_turno(nombre):
    total = 0
    while total < 21:
        total += carta()
        print(f"{nombre} tiene ahora: {total}")
        if nombre == "Jugador":
            eleccion = input("¿Deseas continuar? (s/n): ").strip().lower()
            if eleccion != 's':
                break
        else:
            if total >= 17:
                break
    return total

def evaluar(jugador, pc):
    print(f"\nPuntajes → Jugador: {jugador} | Computadora: {pc}")
    if jugador > 21:
        print("Te pasaste. La computadora gana.")
    elif pc > 21 or jugador > pc:
        print("¡Ganaste!")
    elif jugador < pc:
        print("Perdiste.")
    else:
        print("Empate.")

def inicio():
    print("Bienvenido a Blackjack simplificado")
    j = jugar_turno("Jugador")
    if j <= 21:
        c = jugar_turno("Computadora")
    else:
        c = 0
    evaluar(j, c)

inicio()

