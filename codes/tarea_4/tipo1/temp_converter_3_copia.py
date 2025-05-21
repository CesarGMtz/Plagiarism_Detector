class Temperatura:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def desde_celsius(self):
        return (self.cantidad * 9/5 + 32, self.cantidad + 273.15)

    def desde_fahrenheit(self):
        c = (self.cantidad - 32) * 5/9
        return (c, c + 273.15)

    def desde_kelvin(self):
        c = self.cantidad - 273.15
        return (c, c * 9/5 + 32)

def conversor():
    try:
        cantidad = float(input("Temperatura a convertir: "))
        tipo = input("Ingresa unidad original (C/F/K): ").upper()
        t = Temperatura(cantidad)

        if tipo == "C":
            f, k = t.desde_celsius()
            print(f"{cantidad}°C = {f:.2f}°F y {k:.2f}°K")
        elif tipo == "F":
            c, k = t.desde_fahrenheit()
            print(f"{cantidad}°F = {c:.2f}°C y {k:.2f}°K")
        elif tipo == "K":
            c, f = t.desde_kelvin()
            print(f"{cantidad}°K = {c:.2f}°C y {f:.2f}°F")
        else:
            print("Unidad inválida.")
    except:
        print("Error en entrada de datos.")

conversor()

