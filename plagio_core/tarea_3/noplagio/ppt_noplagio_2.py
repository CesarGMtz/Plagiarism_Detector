import random

def obtener_entrada():
    opcion = input("Juega piedra/papel/tijera: ").strip().lower()
    return opcion

def ganador(usuario, computadora):
    condiciones = [
        (usuario == 'piedra' and computadora == 'tijera'),
        (usuario == 'papel' and computadora == 'piedra'),
        (usuario == 'tijera' and computadora == 'papel')
    ]
    if usuario == computadora:
        return "Empate"
    elif any(condiciones):
        return "Ganas"
    else:
        return "Pierdes"

def iniciar_juego():
    movimientos = ['piedra', 'papel', 'tijera']
    user = obtener_entrada()
    pc = random.choice(movimientos)

    if user not in movimientos:
        print("Entrada inválida.")
        return

    print(f"Computadora eligió: {pc}")
    print(ganador(user, pc))

iniciar_juego()

