import random

class Partida:
    def __init__(self):
        self.palabras = ["algoritmo", "codigo", "debuggear", "archivo"]
        self.meta = random.choice(self.palabras)
        self.intentos = 6
        self.usadas = []

    def juego_activo(self):
        resultado = ""
        for letra in self.meta:
            resultado += letra + " " if letra in self.usadas else "_ "
        print(resultado.strip())

    def iniciar(self):
        print("Iniciando juego...")

        terminado = False
        while not terminado:
            self.juego_activo()
            entrada = input("Ingresa letra: ").lower()

            if entrada in self.usadas:
                print("Letra repetida")
                continue

            self.usadas.append(entrada)

            if entrada not in self.meta:
                self.intentos -= 1
                print("Fallaste. Vidas restantes:", self.intentos)

            if all(c in self.usadas for c in self.meta):
                print("¡Adivinaste! Palabra:", self.meta)
                terminado = True
            elif self.intentos == 0:
                print("Perdiste. Era:", self.meta)
                terminado = True

p = Partida()
p.iniciar()

