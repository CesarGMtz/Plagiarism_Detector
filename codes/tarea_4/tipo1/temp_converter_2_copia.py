def convertir_temperatura(valor, origen):
    if origen == "C":
        return (valor * 9/5 + 32, valor + 273.15)
    elif origen == "F":
        c = (valor - 32) * 5/9
        return (c, c + 273.15)
    elif origen == "K":
        c = valor - 273.15
        return (c, (c * 9/5) + 32)
    return None, None

def ejecutar():
    print("Conversor entre C, F y K.")
    unidad = input("Unidad origen (C/F/K): ").upper()
    try:
        temp = float(input("Temperatura: "))
        salida1, salida2 = convertir_temperatura(temp, unidad)
        if salida1 is None:
            print("Unidad inválida.")
        else:
            print("Valores convertidos:")
            print(f"{salida1:.2f}, {salida2:.2f}")
    except:
        print("Error: dato no numérico.")

ejecutar()

