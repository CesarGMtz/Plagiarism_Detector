import random

def mostrar_palabra(palabra_secreta, letras_usadas):
    resultado = ""
    for caracter in palabra_secreta:
        if caracter in letras_usadas:
            resultado += caracter + " "
        else:
            resultado += "_ "
    print(resultado.strip())

def juego():
    lista_palabras = ["computadora", "programacion", "python", "inteligencia"]
    seleccionada = random.choice(lista_palabras)
    usadas = []
    vidas = 6

    print("Adivina la palabra letra por letra")

    while vidas > 0:
        mostrar_palabra(seleccionada, usadas)
        letra = input("Ingresa una letra: ").lower()

        if letra in seleccionada and letra not in usadas:
            usadas.append(letra)
            if all(c in usadas for c in seleccionada):
                print("¡Ganaste! La palabra era:", seleccionada)
                return
        else:
            vidas -= 1
            print(f"Incorrecto. Te quedan {vidas} intentos.")

    print("Has perdido. La palabra era:", seleccionada)

juego()

