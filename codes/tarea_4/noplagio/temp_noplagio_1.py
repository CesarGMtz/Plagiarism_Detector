def convertir(valor, desde, hacia):
    formulas = {
        ("C", "F"): lambda x: x * 9/5 + 32,
        ("C", "K"): lambda x: x + 273.15,
        ("F", "C"): lambda x: (x - 32) * 5/9,
        ("F", "K"): lambda x: (x - 32) * 5/9 + 273.15,
        ("K", "C"): lambda x: x - 273.15,
        ("K", "F"): lambda x: (x - 273.15) * 9/5 + 32
    }

    if desde == hacia:
        return valor
    return formulas.get((desde, hacia), lambda x: None)(valor)

def main():
    print("Conversor avanzado")
    origen = input("Unidad origen (C/F/K): ").upper()
    destino = input("Unidad destino (C/F/K): ").upper()

    try:
        temp = float(input("Temperatura: "))
        resultado = convertir(temp, origen, destino)
        print(f"{temp}°{origen} = {resultado:.2f}°{destino}")
    except:
        print("Error en datos.")

main()

