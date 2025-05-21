class ConversorTemperatura:
    def __init__(self, valor):
        self.valor = valor

    def celsius(self):
        f = (self.valor * 9/5) + 32
        k = self.valor + 273.15
        return f, k

    def fahrenheit(self):
        c = (self.valor - 32) * 5/9
        k = c + 273.15
        return c, k

    def kelvin(self):
        c = self.valor - 273.15
        f = (c * 9/5) + 32
        return c, f

def main():
    try:
        valor = float(input("Temperatura: "))
        unidad = input("Unidad (C/F/K): ").upper()
        conv = ConversorTemperatura(valor)
        if unidad == "C":
            f, k = conv.celsius()
            print(f"{valor}°C = {f:.2f}°F, {k:.2f}°K")
        elif unidad == "F":
            c, k = conv.fahrenheit()
            print(f"{valor}°F = {c:.2f}°C, {k:.2f}°K")
        elif unidad == "K":
            c, f = conv.kelvin()
            print(f"{valor}°K = {c:.2f}°C, {f:.2f}°F")
        else:
            print("Unidad desconocida.")
    except:
        print("Error en la entrada.")

main()

