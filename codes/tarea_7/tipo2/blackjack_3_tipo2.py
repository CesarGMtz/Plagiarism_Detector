import random

def jugar_blackjack():
    acciones = {
        "jugador": [],
        "computadora": []
    }

    while sum(acciones["jugador"]) <= 21:
        nueva = random.randint(1, 11)
        acciones["jugador"].append(nueva)
        print(f"Jugador recibe: {nueva} → Total: {sum(acciones['jugador'])}")
        if sum(acciones["jugador"]) > 21:
            break
        opc = input("¿Otra carta? (s/n): ").lower()
        if opc != 's':
            break

    while sum(acciones["computadora"]) < 17:
        nueva = random.randint(1, 11)
        acciones["computadora"].append(nueva)
        print(f"Computadora recibe: {nueva} → Total: {sum(acciones['computadora'])}")

    pj = sum(acciones["jugador"])
    pc = sum(acciones["computadora"])
    print(f"\nPuntos finales → Jugador: {pj}, PC: {pc}")
    if pj > 21:
        print("Jugador pierde.")
    elif pc > 21 or pj > pc:
        print("Jugador gana.")
    elif pj < pc:
        print("Computadora gana.")
    else:
        print("Empate.")

jugar_blackjack()

