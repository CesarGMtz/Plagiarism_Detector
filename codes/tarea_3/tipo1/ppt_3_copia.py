import random

def jugar_ppt():
    elecciones = ['piedra', 'papel', 'tijera']
    puntos_user = 0
    puntos_pc = 0

    for ronda in range(3):
        pc = random.choice(elecciones)
        user = input("Escribe piedra, papel o tijera: ").lower()

        if user not in elecciones:
            print("Elección inválida.")
            continue

        print(f"Computadora eligió: {pc}")

        if user == pc:
            print("Empate")
        elif (user == 'piedra' and pc == 'tijera') or \
             (user == 'papel' and pc == 'piedra') or \
             (user == 'tijera' and pc == 'papel'):
            print("¡Ganas esta ronda!")
            puntos_user += 1
        else:
            print("Gana la computadora.")
            puntos_pc += 1

    print(f"Resultado final - Tú: {puntos_user} | PC: {puntos_pc}")

jugar_ppt()

