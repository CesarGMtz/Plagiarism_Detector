import random

def obtener_carta():
    return random.randint(1, 11)

def turno_jugador():
    total = 0
    while True:
        carta = obtener_carta()
        total += carta
        print(f"Recibiste un {carta}. Total actual: {total}")
        if total > 21:
            print("Te pasaste de 21. Pierdes.")
            break
        elif input("¿Otra carta? (s/n): ").lower() != "s":
            break
    return total

def turno_maquina():
    total = 0
    while total < 17:
        carta = obtener_carta()
        total += carta
        print(f"La máquina recibe un {carta}. Total: {total}")
    return total

def determinar_ganador(jugador, maquina):
    if jugador > 21:
        return "La máquina gana."
    elif maquina > 21 or jugador > maquina:
        return "Tú ganas."
    elif jugador == maquina:
        return "Empate."
    return "La máquina gana."

def jugar():
    print("== BLACKJACK ==")
    puntaje_jugador = turno_jugador()
    puntaje_maquina = turno_maquina()
    print(determinar_ganador(puntaje_jugador, puntaje_maquina))

jugar()

