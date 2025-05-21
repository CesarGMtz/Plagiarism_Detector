import random

class Participante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def jugar(self, humano=False):
        while True:
            valor = random.randint(1, 11)
            self.puntaje += valor
            print(f"{self.nombre} saca {valor} → Total: {self.puntaje}")
            if self.puntaje > 21:
                print(f"{self.nombre} perdió.")
                break
            if humano:
                continuar = input("¿Otra carta? (s/n): ").lower()
                if continuar != 's':
                    break
            elif self.puntaje >= 17:
                break

def comenzar_juego():
    print("🔸 Blackjack OOP 🔸")
    p1 = Participante("Tú")
    p2 = Participante("Computadora")
    
    p1.jugar(humano=True)
    if p1.puntaje <= 21:
        p2.jugar()

    print(f"\nResultados finales:")
    print(f"{p1.nombre}: {p1.puntaje} | {p2.nombre}: {p2.puntaje}")
    if p1.puntaje > 21:
        print("Pierdes.")
    elif p2.puntaje > 21 or p1.puntaje > p2.puntaje:
        print("Ganas.")
    elif p1.puntaje < p2.puntaje:
        print("Pierdes.")
    else:
        print("Empate.")

comenzar_juego()

