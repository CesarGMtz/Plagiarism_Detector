import random

def obtener_pista(palabra):
    return f"Empieza con '{palabra[0]}' y tiene {len(palabra)} letras."

def juego():
    banco = ["programa", "memoria", "hardware", "sistema"]
    palabra = random.choice(banco)
    pista = obtener_pista(palabra)
    letras_ingresadas = []

    print("Adivina la palabra. Tendrás una pista inicial.")
    print("Pista:", pista)

    while True:
        intento = input("Ingresa una letra o la palabra completa: ").lower()

        if len(intento) == 1:
            letras_ingresadas.append(intento)
            resultado = "".join([l if l in letras_ingresadas else "_" for l in palabra])
            print("Estado actual:", resultado)
            if "_" not in resultado:
                print("¡Correcto! La palabra era:", palabra)
                break
        elif intento == palabra:
            print("¡Adivinaste toda la palabra!")
            break
        else:
            print("Incorrecto. Sigue intentando.")

juego()

