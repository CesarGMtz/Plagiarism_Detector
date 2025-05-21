def convertir_desde_celsius(c):
    return {
        "F": c * 9/5 + 32,
        "K": c + 273.15
    }

def iniciar_conversion():
    try:
        grados = float(input("Introduce temperatura en Celsius: "))
        resultado = convertir_desde_celsius(grados)
        for unidad, valor in resultado.items():
            print(f"{grados}°C son {valor:.2f}°{unidad}")
    except ValueError:
        print("Error: entrada no válida.")

iniciar_conversion()

