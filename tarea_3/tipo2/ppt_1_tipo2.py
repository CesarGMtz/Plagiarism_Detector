import random

def resultado(jugador, cpu):
    if jugador == cpu:
        return "Empate"
    elif (jugador == 'piedra' and cpu == 'tijera') or \
         (jugador == 'papel' and cpu == 'piedra') or \
         (jugador == 'tijera' and cpu == 'papel'):
        return "Ganaste"
    else:
        return "Perdiste"

def main():
    elecciones = ['piedra', 'papel', 'tijera']
    usuario = input("Escoge piedra, papel o tijera: ").lower()

    if usuario not in elecciones:
        print("Entrada inválida")
        return

    maquina = random.choice(elecciones)
    print(f"La máquina eligió: {maquina}")
    print(resultado(usuario, maquina))

main()

