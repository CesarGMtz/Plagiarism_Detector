class Celsius:
    def __init__(self, valor):
        self.valor = valor

    def a_f(self):
        return self.valor * 9/5 + 32

    def a_k(self):
        return self.valor + 273.15

class Fahrenheit:
    def __init__(self, valor):
        self.valor = valor

    def a_c(self):
        return (self.valor - 32) * 5/9

    def a_k(self):
        return self.a_c() + 273.15

class Kelvin:
    def __init__(self, valor):
        self.valor = valor

    def a_c(self):
        return self.valor - 273.15

    def a_f(self):
        return self.a_c() * 9/5 + 32

def ejecutar():
    unidad = input("Desde (C/F/K): ").upper()
    valor = float(input("Valor: "))
    
    if unidad == "C":
        c = Celsius(valor)
        print(f"F: {c.a_f():.2f}, K: {c.a_k():.2f}")
    elif unidad == "F":
        f = Fahrenheit(valor)
        print(f"C: {f.a_c():.2f}, K: {f.a_k():.2f}")
    elif unidad == "K":
        k = Kelvin(valor)
        print(f"C: {k.a_c():.2f}, F: {k.a_f():.2f}")
    else:
        print("Unidad no reconocida.")

ejecutar()

