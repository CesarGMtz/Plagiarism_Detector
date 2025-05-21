import random

def palabra_aleatoria():
    palabras = ["variable", "funcion", "bucle", "condicional"]
    return random.choice(palabras)

def estado_actual(letras_adivinadas, palabra_objetivo):
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra_objetivo)

def ejecutar_juego():
    secreta = palabra_aleatoria()
    correctas = set()
    usadas = set()
    oportunidades = 7

    print("Comenzando el juego...")

    while oportunidades > 0:
        print(estado_actual(correctas, secreta))
        entrada = input("Letra: ").lower()

        if entrada in usadas:
            print("Letra ya usada.")
            continue

        usadas.add(entrada)

        if entrada in secreta:
            correctas.add(entrada)
            if set(secreta).issubset(correctas):
                print(f"¡Ganaste! Palabra: {secreta}")
                return
        else:
            oportunidades -= 1
            print("Letra equivocada. Te quedan:", oportunidades)

    print(f"Game Over. Palabra correcta: {secreta}")

ejecutar_juego()

