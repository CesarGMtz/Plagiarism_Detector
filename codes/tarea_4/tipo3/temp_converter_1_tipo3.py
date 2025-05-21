def convertir_celsius_a_fahrenheit(grados):
    return (grados * 9 / 5) + 32

def convertir_celsius_a_kelvin(grados):
    return grados + 273.15

def solicitar_temperatura():
    try:
        return float(input("Temperatura en °C: "))
    except ValueError:
        print("Entrada no válida.")
        return None

def mostrar_resultados(c):
    print(f"{c}°C equivale a {convertir_celsius_a_fahrenheit(c)}°F")
    print(f"{c}°C equivale a {convertir_celsius_a_kelvin(c)}K")

def ciclo():
    while True:
        celsius = solicitar_temperatura()
        if celsius is None:
            continue
        mostrar_resultados(celsius)
        if input("¿Salir? (s/n): ").lower() == "s":
            break

ciclo()

