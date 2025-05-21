import random

def obtener_palabra():
    palabras = ["variable", "funcion", "bucle", "python", "modulo"]
    return random.choice(palabras)

def estado_actual(palabra, adivinadas):
    return " ".join([letra if letra in adivinadas else "_" for letra in palabra])

def jugar():
    palabra = obtener_palabra()
    adivinadas = set()
    intentos = 6

    while intentos > 0:
        print("\nPalabra:", estado_actual(palabra, adivinadas))
        letra = input("Adivina una letra: ").lower()

        if letra in adivinadas:
            print("Ya adivinaste esa letra.")
            continue

        adivinadas.add(letra)

        if letra in palabra:
            if all(l in adivinadas for l in palabra):
                print("¡Ganaste! La palabra era:", palabra)
                break
        else:
            intentos -= 1
            print(f"Incorrecto. Intentos restantes: {intentos}")

    if intentos == 0:
        print("Perdiste. La palabra era:", palabra)

jugar()

