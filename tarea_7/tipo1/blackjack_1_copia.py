import random

def sacar_carta():
    return random.randint(1, 11)

def turno_usuario():
    suma = 0
    while True:
        nueva = sacar_carta()
        suma += nueva
        print(f"Carta: {nueva}, total: {suma}")
        if suma > 21:
            print("Te pasaste. Fin del juego.")
            return suma
        seguir = input("¿Deseas otra carta? (s/n): ").lower()
        if seguir != 's':
            break
    return suma

def turno_pc():
    suma = 0
    while suma < 17:
        carta = sacar_carta()
        suma += carta
        print(f"PC saca: {carta}, total: {suma}")
    return suma

def juego():
    print("Comienza Blackjack")
    usuario = turno_usuario()
    if usuario > 21:
        return
    pc = turno_pc()
    if pc > 21 or usuario > pc:
        print("Ganaste tú.")
    elif usuario < pc:
        print("Gana la PC.")
    else:
        print("Empate.")

juego()

