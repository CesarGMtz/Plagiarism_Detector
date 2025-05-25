import random

def seleccionar_objetivo():
    lista = ["algoritmo", "codigo", "debuggear", "archivo"]
    return random.choice(lista)

def estado_actual(palabra, descubiertas):
    return [letra if letra in descubiertas else "_" for letra in palabra]

def jugar(partida):
    palabra = partida["palabra"]
    errores = 0
    max_errores = 6
    letras = []

    while True:
        estado = estado_actual(palabra, letras)
        print(" ".join(estado))

        if "_" not in estado:
            print("¡Has ganado! La palabra era:", palabra)
            break

        if errores >= max_errores:
            print("Sin vidas. Palabra:", palabra)
            break

        intento = input("Letra: ").lower()

        if intento in letras:
            print("Ya la usaste.")
            continue

        letras.append(intento)

        if intento not in palabra:
            errores += 1
            print(f"Fallaste. Errores: {errores}/{max_errores}")

def iniciar_juego():
    juego = {"palabra": seleccionar_objetivo()}
    jugar(juego)

iniciar_juego()

