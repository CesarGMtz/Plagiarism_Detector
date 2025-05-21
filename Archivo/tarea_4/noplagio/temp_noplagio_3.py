def convertir_temp():
    tabla = {
        "C": lambda x: (x * 9/5 + 32, x + 273.15),
        "F": lambda x: ((x - 32) * 5/9, (x - 32) * 5/9 + 273.15),
        "K": lambda x: (x - 273.15, (x - 273.15) * 9/5 + 32)
    }

    entrada = input("Ingresa unidad (C, F, K): ").upper()
    if entrada not in tabla:
        print("Unidad incorrecta.")
        return

    try:
        cantidad = float(input("Temperatura: "))
        r1, r2 = tabla[entrada](cantidad)
        if entrada == "C":
            print(f"{cantidad}°C -> {r1:.2f}°F, {r2:.2f}°K")
        elif entrada == "F":
            print(f"{cantidad}°F -> {r1:.2f}°C, {r2:.2f}°K")
        elif entrada == "K":
            print(f"{cantidad}°K -> {r1:.2f}°C, {r2:.2f}°F")
    except:
        print("Error en entrada.")

convertir_temp()

