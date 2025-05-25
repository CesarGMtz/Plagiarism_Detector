def convertir_a_fahrenheit(grados):
    return grados * 9 / 5 + 32

def convertir_a_kelvin(grados):
    return grados + 273.15

def iniciar():
    try:
        entrada = float(input("Temperatura en Celsius: "))
        faren = convertir_a_fahrenheit(entrada)
        kel = convertir_a_kelvin(entrada)

        print(f"{entrada}°C = {faren:.2f}°F")
        print(f"{entrada}°C = {kel:.2f}°K")
    except ValueError:
        print("Error: ingresa un valor numérico.")

iniciar()

