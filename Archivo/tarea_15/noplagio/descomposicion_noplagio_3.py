import random

def jugar_turnos():
    palabras = ["archivo", "procesador", "mouse", "ventana"]
    palabra = random.choice(palabras)
    letras = set(palabra)
    adivinadas = set()
    total_turnos = 10

    print(f"Desafío: Adivina la palabra en {total_turnos} turnos.")

    for turno in range(1, total_turnos + 1):
        letra = input(f"Turno {turno} - Ingresa letra: ").lower()

        if letra in letras:
            adivinadas.add(letra)
            print("¡Bien! Letra correcta.")
        else:
            print("Letra no está.")

        progreso = [c if c in adivinadas else "_" for c in palabra]
        print("Progreso:", " ".join(progreso))

        if letras.issubset(adivinadas):
            print("¡Victoria! Descubriste la palabra:", palabra)
            return

    print("Se acabaron los turnos. Era:", palabra)

jugar_turnos()

