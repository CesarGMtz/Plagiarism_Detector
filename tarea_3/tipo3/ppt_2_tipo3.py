import random

def mostrar_menu():
    print("=== PIEDRA PAPEL O TIJERA ===")

def pedir_entrada_usuario():
    eleccion = input("Tu jugada (piedra/papel/tijera): ").strip().lower()
    return eleccion

def jugar_ronda(usuario, cpu):
    print(f"Computadora elige: {cpu}")
    if usuario == cpu:
        return "Empate"
    elif (usuario == "piedra" and cpu == "tijera") or \
         (usuario == "papel" and cpu == "piedra") or \
         (usuario == "tijera" and cpu == "papel"):
        return "Usuario gana"
    return "Computadora gana"

def bucle_principal():
    opciones = ["piedra", "papel", "tijera"]
    while True:
        mostrar_menu()
        usuario = pedir_entrada_usuario()
        if usuario not in opciones:
            print("Opción inválida. Intenta de nuevo.")
            continue
        cpu = random.choice(opciones)
        resultado = jugar_ronda(usuario, cpu)
        print("Resultado:", resultado)
        if input("¿Salir? (s/n): ").lower() == "s":
            break

bucle_principal()

