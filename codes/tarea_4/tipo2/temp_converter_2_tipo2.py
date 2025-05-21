def convertir(valor, origen):
    conversiones = {
        "C": lambda v: ((v * 9/5 + 32), (v + 273.15)),
        "F": lambda v: (((v - 32) * 5/9), ((v - 32) * 5/9 + 273.15)),
        "K": lambda v: ((v - 273.15), ((v - 273.15) * 9/5 + 32))
    }
    return conversiones.get(origen, lambda v: (None, None))(valor)

def ejecutar_conversion():
    unidad = input("Origen (C/F/K): ").upper()
    try:
        temp = float(input("Valor: "))
        r1, r2 = convertir(temp, unidad)
        if r1 is None:
            print("Unidad no soportada.")
        else:
            print(f"Resultado 1: {r1:.2f}, Resultado 2: {r2:.2f}")
    except:
        print("Error en entrada.")

ejecutar_conversion()

