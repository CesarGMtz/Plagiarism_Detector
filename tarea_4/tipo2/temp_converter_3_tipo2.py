def celsius(f, k):
    return f"°C = {f:.2f}°F y {k:.2f}°K"

def fahrenheit(c, k):
    return f"°F = {c:.2f}°C y {k:.2f}°K"

def kelvin(c, f):
    return f"°K = {c:.2f}°C y {f:.2f}°F"

def controlador(valor, tipo):
    if tipo == "C":
        return celsius(valor * 9/5 + 32, valor + 273.15)
    elif tipo == "F":
        c = (valor - 32) * 5/9
        return fahrenheit(c, c + 273.15)
    elif tipo == "K":
        c = valor - 273.15
        return kelvin(c, c * 9/5 + 32)
    else:
        return "Unidad no reconocida."

def conversor():
    try:
        dato = float(input("Temperatura: "))
        unidad = input("Unidad (C/F/K): ").upper()
        print(controlador(dato, unidad))
    except:
        print("Entrada inválida.")

conversor()

