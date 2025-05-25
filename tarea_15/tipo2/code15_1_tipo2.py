import random

def mostrar_progreso(palabra, encontradas):
    resultado = ""
    for c in palabra:
        resultado += c + " " if c in encontradas else "_ "
    print(resultado.strip())

def jugar_ahorcado():
    lista_palabras = ["computadora", "programacion", "python", "inteligencia"]
    oculta = random.choice(lista_palabras)
    usadas = []
    vidas = 6

    print("=== Ahorcado ===")

    while vidas > 0:
        mostrar_progreso(oculta, usadas)
        letra = input("Ingresa una letra: ").lower()

        if letra in oculta and letra not in usadas:
            usadas.append(letra)
            if all(l in usadas for l in oculta):
                print(f"¡Ganaste! La palabra era: {oculta}")
                return
        else:
            vidas -= 1
            print(f"Fallaste. Intentos restantes: {vidas}")

    print(f"Has perdido. La palabra correcta era: {oculta}")

jugar_ahorcado()

