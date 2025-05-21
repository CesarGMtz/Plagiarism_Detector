import random

class SimuladorDados:
    def __init__(self, repeticiones):
        self.repeticiones = repeticiones
        self.resultados = {i: 0 for i in range(1, 7)}

    def lanzar(self):
        return random.randint(1, 6)

    def ejecutar(self):
        for _ in range(self.repeticiones):
            r = self.lanzar()
            self.resultados[r] += 1

    def mostrar(self):
        print("Distribución:")
        for cara, cantidad in self.resultados.items():
            print(f"{cara}: {cantidad}")

def pedir_repeticiones():
    try:
        return int(input("¿Cuántos lanzamientos deseas simular? "))
    except ValueError:
        return 0

def main():
    while True:
        veces = pedir_repeticiones()
        if veces <= 0:
            print("Valor inválido.")
            continue
        simulador = SimuladorDados(veces)
        simulador.ejecutar()
        simulador.mostrar()
        if input("¿Salir? (s/n): ").lower() == "s":
            break

main()

