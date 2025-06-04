def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.15

def main():
    try:
        c = float(input("Ingresa temperatura en °C: "))
        f = celsius_a_fahrenheit(c)
        k = celsius_a_kelvin(c)
        print(f"{c}°C equivale a {f:.2f}°F")
        print(f"{c}°C equivale a {k:.2f}°K")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")

main()

