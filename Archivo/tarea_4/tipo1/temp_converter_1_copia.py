def a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def a_kelvin(celsius):
    return celsius + 273.15

def inicio():
    try:
        grado = float(input("Introduce la temperatura en Celsius: "))
        fahrenheit = a_fahrenheit(grado)
        kelvin = a_kelvin(grado)
        print(f"{grado} grados Celsius equivalen a {kelvin:.2f} Kelvin")
        print(f"{grado} grados Celsius equivalen a {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        print("Por favor ingresa un número válido.")

inicio()

