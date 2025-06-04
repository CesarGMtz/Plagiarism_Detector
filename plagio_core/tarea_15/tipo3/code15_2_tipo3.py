import random

def escoger_palabra():
    return random.choice(["variable", "funcion", "bucle", "condicional"])

def verificar_ganador(palabra, aciertos):
    return all(letra in aciertos for letra in palabra)

def imprimir_estado(palabra, aciertos):
    print(" ".join(letra if letra in aciertos else "_" for letra in palabra))

def solicitar_letra(letras_intentadas):
    while True:
        letra = input("Introduce una letra: ").strip().lower()
        if letra not in letras_intentadas:
            return letra
        print("Letra repetida.")

def iniciar():
    palabra = escoger_palabra()
    aciertos = set()
    intentos = 7
    letras_usadas = set()

    while intentos:
        imprimir_estado(palabra, aciertos)

        if verificar_ganador(palabra, aciertos):
            print("¡Victoria! Palabra:", palabra)
            return

        letra = solicitar_letra(letras_usadas)
        letras_usadas.add(letra)

        if letra in palabra:
            aciertos.add(letra)
        else:
            intentos -= 1
            print("Incorrecto. Restan:", intentos)

    print("Fracaso. Palabra:", palabra)

iniciar()

