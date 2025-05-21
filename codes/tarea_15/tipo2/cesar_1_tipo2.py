import random

def imprimir_ocultas(palabra, visibles):
    ocultas = ["_" if letra not in visibles else letra for letra in palabra]
    print(" ".join(ocultas))

def iniciar_ahorcado():
    palabras_juego = ["computadora", "programacion", "python", "inteligencia"]
    palabra = random.choice(palabras_juego)
    visibles = []
    fallos = 0

    print("Comienza el reto del ahorcado.")

    while True:
        imprimir_ocultas(palabra, visibles)

        if all(letra in visibles for letra in palabra):
            print("¡Correcto! La palabra es:", palabra)
            break

        if fallos >= 6:
            print("Fallaste. La palabra era:", palabra)
            break

        letra = input("Letra: ").strip().lower()

        if letra not in palabra:
            fallos += 1
            print("Letra no encontrada. Fallos:", fallos)
        elif letra not in visibles:
            visibles.append(letra)
        else:
            print("Letra ya revelada.")

iniciar_ahorcado()

