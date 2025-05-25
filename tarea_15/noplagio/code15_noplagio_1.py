import random

def iniciar_juego():
    palabras = ["monitor", "raton", "teclado", "pantalla"]
    seleccionada = random.choice(palabras)
    ocultas = ["_"] * len(seleccionada)
    descubiertas = set()

    print("Adivina todas las letras sin límite de intentos")

    while "_" in ocultas:
        print("Palabra:", " ".join(ocultas))
        letra = input("Letra: ").lower()

        if letra in descubiertas:
            print("Letra ya ingresada.")
            continue

        descubiertas.add(letra)

        for i, l in enumerate(seleccionada):
            if l == letra:
                ocultas[i] = letra

    print(f"¡Felicidades! Descubriste: {seleccionada}")

iniciar_juego()

