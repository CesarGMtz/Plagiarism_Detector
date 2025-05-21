def transformar_decimal(valor):
    bin_ = bin(valor)[2:]
    oct_ = oct(valor)[2:]
    hex_ = hex(valor)[2:].upper()

    print(f"Entrada: {valor}")
    print(f"En binario: {bin_}")
    print(f"En octal: {oct_}")
    print(f"En hexadecimal: {hex_}")

def ejecutar():
    print("== CONVERSOR DE BASES ==")
    try:
        numero_usuario = int(input("Número decimal a convertir: "))
        if numero_usuario < 0:
            print("Solo se admiten valores positivos.")
            return
        transformar_decimal(numero_usuario)
    except ValueError:
        print("Error: entrada no válida.")

ejecutar()