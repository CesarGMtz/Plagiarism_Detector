class Convertidor:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def desde_celsius(self):
        f = (self.cantidad * 9 / 5) + 32
        k = self.cantidad + 273.15
        return f, k

    def desde_fahrenheit(self):
        c = (self.cantidad - 32) * 5 / 9
        k = c + 273.15
        return c, k

    def desde_kelvin(self):
        c = self.cantidad - 273.15
        f = (c * 9 / 5) + 32
        return c, f

def iniciar():
    try:
        valor = float(input("Introduce temperatura: "))
        tipo = input("Unidad de origen (C/F/K): ").upper()
        conv = Convertidor(valor)

        if tipo == "C":
            f, k = conv.desde_celsius()
            print(f"{valor}°C equivale a {f:.2f}°F y {k:.2f}°K")
        elif tipo == "F":
            c, k = conv.desde_fahrenheit()
            print(f"{valor}°F equivale a {c:.2f}°C y {k:.2f}°K")
        elif tipo == "K":
            c, f = conv.desde_kelvin()
            print(f"{valor}°K equivale a {c:.2f}°C y {f:.2f}°F")
        else:
            print("Unidad no válida.")
    except:
        print("Entrada inválida.")

iniciar()

