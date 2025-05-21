import random

def sacar_carta():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

def turno_persona():
    suma = 0
    while suma < 21:
        suma += sacar_carta()
        print("→ Tu total actual:", suma)
        if suma >= 21:
            break
        opc = input("¿Otra carta? (s/n): ")
        if opc.lower() != 's':
            break
    return suma

def turno_pc():
    puntos = 0
    while puntos < 17:
        puntos += sacar_carta()
    return puntos

def resultado(j, c):
    print(f"\nResultado final - Jugador: {j} | PC: {c}")
    if j > 21:
        print("Te pasaste, pierdes.")
    elif c > 21 or j > c:
        print("Ganaste.")
    elif j < c:
        print("Perdiste.")
    else:
        print("Empate.")

def main():
    j = turno_persona()
    c = turno_pc() if j <= 21 else 0
    resultado(j, c)

main()

