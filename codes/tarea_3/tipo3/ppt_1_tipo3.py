import random

def obtener_opciones():
    return ['piedra', 'papel', 'tijera']

def elegir_computadora(opciones):
    return random.choice(opciones)

def evaluar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def pedir_jugada():
    try:
        jugada = input("Tu elección (piedra, papel, tijera): ").lower()
        if jugada not in obtener_opciones():
            raise ValueError("Opción no válida.")
        return jugada
    except Exception as e:
        print(f"Error: {e}")
        return None

def jugar():
    while True:
        jugador = pedir_jugada()
        if not jugador:
            continue
        computadora = elegir_computadora(obtener_opciones())
        print(f"Computadora eligió: {computadora}")
        print(evaluar_ganador(jugador, computadora))
        salir = input("¿Quieres salir? (s/n): ")
        if salir.lower() == 's':
            break

jugar()

