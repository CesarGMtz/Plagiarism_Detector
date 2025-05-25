import random

def seleccionar_palabra():
    opciones = ["variable", "funcion", "bucle", "condicional"]
    return random.choice(opciones)

def progreso_actual(palabra, adivinadas):
    return " ".join([c if c in adivinadas else "_" for c in palabra])

def iniciar_juego():
    secreta = seleccionar_palabra()
    descubiertas = set()
    intentadas = set()
    oportunidades = 7

    print("== Bienvenido al juego del Ahorcado ==")

    while oportunidades > 0:
        print(progreso_actual(secreta, descubiertas))
        intento = input("Letra: ").lower()

        if intento in intentadas:
            print("Ya escribiste esa letra antes.")
            continue

        intentadas.add(intento)

        if intento in secreta:
            descubiertas.add(intento)
            if set(secreta).issubset(descubiertas):
                print(f"¡Victoria! La palabra era: {secreta}")
                return
        else:
            oportunidades -= 1
            print(f"Letra incorrecta. Intentos restantes: {oportunidades}")

    print(f"¡Derrota! La palabra correcta era: {secreta}")

iniciar_juego()

