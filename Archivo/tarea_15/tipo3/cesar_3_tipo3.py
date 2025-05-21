import random

class JuegoAhorcado:
    def __init__(self):
        self.palabras = ["codigo", "editor", "juego", "teclado", "pantalla"]
        self.palabra = random.choice(self.palabras)
        self.adivinadas = set()
        self.intentos = 6

    def mostrar_estado(self):
        print(" ".join([l if l in self.adivinadas else "_" for l in self.palabra]))

    def jugar(self):
        while self.intentos > 0:
            self.mostrar_estado()
            intento = input("Ingresa una letra: ").lower()

            if intento in self.adivinadas:
                print("Ya usaste esa letra.")
                continue

            self.adivinadas.add(intento)

            if intento not in self.palabra:
                self.intentos -= 1
                print(f"Incorrecto. Te quedan {self.intentos} intentos.")
            elif all(l in self.adivinadas for l in self.palabra):
                print("¡Ganaste! La palabra era:", self.palabra)
                return

        print("Has perdido. La palabra era:", self.palabra)

def main():
    juego = JuegoAhorcado()
    juego.jugar()

main()

