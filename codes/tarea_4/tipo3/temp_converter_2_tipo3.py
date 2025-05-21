def convertir(temperatura, unidad_origen, unidad_destino):
    if unidad_origen == "C":
        if unidad_destino == "F":
            return (temperatura * 9/5) + 32
        elif unidad_destino == "K":
            return temperatura + 273.15
    elif unidad_origen == "F":
        if unidad_destino == "C":
            return (temperatura - 32) * 5/9
        elif unidad_destino == "K":
            return ((temperatura - 32) * 5/9) + 273.15
    elif unidad_origen == "K":
        if unidad_destino == "C":
            return temperatura - 273.15
        elif unidad_destino == "F":
            return ((temperatura - 273.15) * 9/5) + 32
    return None

def leer_entrada():
    try:
        temp = float(input("Ingresa la temperatura: "))
        origen = input("Unidad de origen (C/F/K): ").strip().upper()
        destino = input("Unidad de destino (C/F/K): ").strip().upper()
        return temp, origen, destino
    except:
        print("Error en la entrada.")
        return None, None, None

def ejecutar():
    while True:
        t, o, d = leer_entrada()
        if t is None or o not in ["C", "F", "K"] or d not in ["C", "F", "K"]:
            print("Datos inválidos. Intenta otra vez.")
            continue
        resultado = convertir(t, o, d)
        if resultado is not None:
            print(f"Resultado: {resultado:.2f}°{d}")
        else:
            print("Conversión no soportada.")
        if input("¿Salir? (s/n): ").lower() == "s":
            break

ejecutar()

