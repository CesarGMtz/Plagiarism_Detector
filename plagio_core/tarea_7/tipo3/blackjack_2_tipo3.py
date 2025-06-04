import random

def carta():
    return random.choice(range(2, 12))

def jugar_turno(entidad):
    total = 0
    while total < 17:
        c = carta()
        total += c
        print(f"{entidad} recibió un {c}. Total: {total}")
        if entidad == "Jugador":
            if total >= 21 or input("¿Pedir carta? (s/n): ").lower() != "s":
                break
    return total

def evaluar(j, m):
    if j > 21:
        return "Perdiste"
    if m > 21 or j > m:
        return "Ganaste"
    if j == m:
        return "Empate"
    return "Perdiste"

def main():
    jugador = jugar_turno("Jugador")
    maquina = jugar_turno("Máquina")
    print(evaluar(jugador, maquina))

main()

