import random

class Ahorcado:
    def __init__(self):
        self.palabras = ["algoritmo", "codigo", "debuggear", "archivo"]
        self.palabra = random.choice(self.palabras)
        self.intentos = 6
        self.adivinadas = set()

    def mostrar_estado(self):
        estado = [letra if letra in self.adivinadas else "_" for letra in self.palabra]
        print(" ".join(estado))

    def jugar(self):
        print("¡Comienza el juego del Ahorcado!")

        while self.intentos > 0:
            self.mostrar_estado()
            letra = input("Ingresa una letra: ").lower()

            if letra in self.adivinadas:
                print("Ya usaste esa letra.")
                continue

            self.adivinadas.add(letra)

            if letra not in self.palabra:
                self.intentos -= 1
                print(f"Letra incorrecta. Intentos restantes: {self.intentos}")

            if all(letra in self.adivinadas for letra in self.palabra):
                print(f"¡Ganaste! La palabra era: {self.palabra}")
                return

        print(f"Perdiste. La palabra era: {self.palabra}")

juego = Ahorcado()
juego.jugar()

