import random

class JuegoAhorcado:
    def __init__(self):
        self.opciones = ["algoritmo", "codigo", "debuggear", "archivo"]
        self.oculta = random.choice(self.opciones)
        self.vidas = 6
        self.usadas = set()

    def imprimir_tablero(self):
        palabra_mostrada = [c if c in self.usadas else "_" for c in self.oculta]
        print(" ".join(palabra_mostrada))

    def comenzar(self):
        print("¡A jugar Ahorcado!")

        while self.vidas > 0:
            self.imprimir_tablero()
            entrada = input("Letra: ").lower()

            if entrada in self.usadas:
                print("Letra repetida.")
                continue

            self.usadas.add(entrada)

            if entrada not in self.oculta:
                self.vidas -= 1
                print(f"Incorrecto. Vidas: {self.vidas}")

            if all(char in self.usadas for char in self.oculta):
                print("¡Felicidades! Palabra:", self.oculta)
                return

        print("Perdiste. Era:", self.oculta)

partida = JuegoAhorcado()
partida.comenzar()

