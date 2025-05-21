import random

def inicializar_juego():
    return {
        "palabra": random.choice(["computadora", "programacion", "python", "inteligencia"]),
        "vidas": 6,
        "usadas": set(),
    }

def obtener_estado(palabra, usadas):
    return [letra if letra in usadas else "_" for letra in palabra]

def bucle_juego(juego):
    while juego["vidas"] > 0:
        estado = obtener_estado(juego["palabra"], juego["usadas"])
        print(" ".join(estado))

        if "_" not in estado:
            print("¡Ganaste! Era:", juego["palabra"])
            return

        entrada = input("Letra: ").lower()
        if entrada in juego["usadas"]:
            print("Ya la usaste.")
            continue

        juego["usadas"].add(entrada)

        if entrada not in juego["palabra"]:
            juego["vidas"] -= 1
            print(f"Incorrecto. Te quedan {juego['vidas']} vidas.")

    print("Has perdido. Palabra:", juego["palabra"])

def main():
    juego = inicializar_juego()
    bucle_juego(juego)

main()

