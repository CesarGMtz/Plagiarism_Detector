import random

def seleccionar():
    return random.choice(["variable", "funcion", "bucle", "condicional"])

def ocultar(palabra, letras):
    salida = ""
    for i in palabra:
        salida += i + " " if i in letras else "_ "
    return salida.strip()

def main():
    objetivo = seleccionar()
    correctas = set()
    intentadas = set()
    restantes = 7

    print("Empieza el juego del ahorcado.")

    while restantes:
        estado = ocultar(objetivo, correctas)
        print(estado)

        if "_" not in estado:
            print("¡Ganaste! La palabra es:", objetivo)
            return

        letra = input("Introduce una letra: ").lower()

        if letra in intentadas:
            print("Ya intentaste esa letra.")
        else:
            intentadas.add(letra)
            if letra in objetivo:
                correctas.add(letra)
            else:
                restantes -= 1
                print("Incorrecta. Te quedan", restantes, "vidas.")

    print("Derrota. Palabra:", objetivo)

main()

