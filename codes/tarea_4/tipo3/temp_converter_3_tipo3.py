class ConversorDeTemperatura:
    def __init__(self, valor):
        self.valor = valor

    def c_a_f(self):
        return (self.valor * 9 / 5) + 32

    def c_a_k(self):
        return self.valor + 273.15

    def mostrar_todo(self):
        print(f"{self.valor}°C en Fahrenheit: {self.c_a_f():.2f}°F")
        print(f"{self.valor}°C en Kelvin: {self.c_a_k():.2f}K")

def leer_valor():
    try:
        return float(input("Temperatura en grados Celsius: "))
    except ValueError:
        print("Entrada inválida.")
        return None

def interfaz():
    while True:
        temp = leer_valor()
        if temp is None:
            continue
        c = ConversorDeTemperatura(temp)
        c.mostrar_todo()
        if input("¿Salir? (s/n): ").lower() == "s":
            break

interfaz()

