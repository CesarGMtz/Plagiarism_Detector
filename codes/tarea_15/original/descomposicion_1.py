import random

def elegir_palabra():
    lista = ["variable", "funcion", "bucle", "condicional"]
    return random.choice(lista)

def actualizar_progreso(palabra, letras):
    return " ".join([letra if letra in letras else "_" for letra in palabra])

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_correctas = set()
    letras_intentadas = set()
    vidas = 7

    print("¡Adivina la palabra!")

    while vidas > 0:
        print(actualizar_progreso(palabra, letras_correctas))
        letra = input("Introduce una letra: ").lower()

        if letra in letras_intentadas:
            print("Ya intentaste esa letra.")
            continue

        letras_intentadas.add(letra)

        if letra in palabra:
            letras_correctas.add(letra)
            if set(palabra).issubset(letras_correctas):
                print(f"¡Ganaste! La palabra era: {palabra}")
                return
        else:
            vidas -= 1
            print(f"Incorrecto. Vidas restantes: {vidas}")

    print(f"Perdiste. La palabra era: {palabra}")

jugar_ahorcado()

