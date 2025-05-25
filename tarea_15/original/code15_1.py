import random

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print(tablero.strip())

def jugar():
    palabras = ["computadora", "programacion", "python", "inteligencia"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego de Ahorcado!")

    while intentos > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        intento = input("Adivina una letra: ").lower()

        if intento in palabra_secreta and intento not in letras_adivinadas:
            letras_adivinadas.append(intento)
            if all(letra in letras_adivinadas for letra in palabra_secreta):
                print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
                return
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

    print(f"Perdiste. La palabra era: {palabra_secreta}")

jugar()

