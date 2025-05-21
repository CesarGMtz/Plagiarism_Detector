import random

def elegir_palabra():
    return random.choice(["computadora", "programa", "código", "juego", "terminal"])

def mostrar(palabra, adivinadas):
    return " ".join([letra if letra in adivinadas else "_" for letra in palabra])

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    errores = 0
    max_errores = 7

    while errores < max_errores:
        print("\n", mostrar(palabra, letras_adivinadas))
        letra = input("Letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya ingresaste esa letra.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra:
            if all(c in letras_adivinadas for c in palabra):
                print("¡Ganaste! Palabra:", palabra)
                return
        else:
            errores += 1
            print("Fallaste. Intentos restantes:", max_errores - errores)

    print("Perdiste. Palabra era:", palabra)

jugar_ahorcado()

