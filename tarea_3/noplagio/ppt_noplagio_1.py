import random

jugadas = {1: 'piedra', 2: 'papel', 3: 'tijera'}

def mostrar_menu():
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

def determinar_ganador(user, cpu):
    if user == cpu:
        return "Empate"
    elif (user == 1 and cpu == 3) or (user == 2 and cpu == 1) or (user == 3 and cpu == 2):
        return "Ganaste"
    else:
        return "Perdiste"

def main():
    mostrar_menu()
    try:
        eleccion = int(input("Elige tu jugada (1-3): "))
        if eleccion not in jugadas:
            print("Selección inválida.")
            return
        pc = random.randint(1, 3)
        print(f"Computadora eligió: {jugadas[pc]}")
        print(determinar_ganador(eleccion, pc))
    except ValueError:
        print("Ingresa un número.")

main()

