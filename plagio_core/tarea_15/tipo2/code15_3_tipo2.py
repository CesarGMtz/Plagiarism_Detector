import random

class JuegoAhorcado:
    def __init__(self):
        self.opciones = ["algoritmo", "codigo", "debuggear", "archivo"]
        self.secreta = random.choice(self.opciones)
        self.vidas = 6
        self.letras_usadas = set()

    def ver_tablero(self):
        progreso = [c if c in self.letras_usadas else "_" for c in self.secreta]
        print(" ".join(progreso))

    def iniciar(self):
        print("=== Ahorcado OO ===")

        while self.vidas > 0:
            self.ver_tablero()
            intento = input("Letra: ").lower()

            if intento in self.letras_usadas:
                print("Ya intentaste esa.")
                continue

            self.letras_usadas.add(intento)

            if intento not in self.secreta:
                self.vidas -= 1
                print(f"Incorrecto. Vidas: {self.vidas}")

            if all(c in self.letras_usadas for c in self.secreta):
                print(f"¡Ganaste! Era: {self.secreta}")
                return

        print(f"Perdiste. La palabra era: {self.secreta}")

jugar = JuegoAhorcado()
jugar.iniciar()

