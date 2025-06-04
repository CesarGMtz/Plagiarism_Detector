def transformar(valor, unidad):
    if unidad == "C":
        return (valor * 9 / 5) + 32, valor + 273.15
    elif unidad == "F":
        c = (valor - 32) * 5 / 9
        return c, c + 273.15
    elif unidad == "K":
        c = valor - 273.15
        return c, (c * 9 / 5) + 32
    return None, None

def iniciar():
    print("== Conversión de Temperaturas ==")
    print("Opciones: C (Celsius), F (Fahrenheit), K (Kelvin)")
    origen = input("Ingresa unidad de origen: ").strip().upper()

    try:
        cantidad = float(input("Valor numérico: "))
        t1, t2 = transformar(cantidad, origen)
        if t1 is None:
            print("Unidad desconocida.")
        else:
            print(f"Equivalentes: {t1:.2f}, {t2:.2f}")
    except:
        print("Entrada inválida.")

iniciar()

