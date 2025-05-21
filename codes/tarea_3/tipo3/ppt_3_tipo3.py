import random

def definir_opciones():
    return ['piedra', 'papel', 'tijera']

def entrada_usuario():
    try:
        return input("Selecciona piedra, papel o tijera: ").lower()
    except:
        return ""

def entrada_valida(eleccion, opciones):
    return eleccion in opciones

def ronda(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == 'piedra' and maquina == 'tijera') or \
         (jugador == 'papel' and maquina == 'piedra') or \
         (jugador == 'tijera' and maquina == 'papel'):
        return "Ganaste esta ronda"
    return "Perdiste esta ronda"

def loop_juego():
    opciones = definir_opciones()
    while True:
        user = entrada_usuario()
        if not entrada_valida(user, opciones):
            print("Entrada inválida.")
            continue
        cpu = random.choice(opciones)
        print(f"La computadora eligió: {cpu}")
        print(ronda(user, cpu))
        if input("¿Terminar partida? (s/n): ").lower() == 's':
            break

loop_juego()

