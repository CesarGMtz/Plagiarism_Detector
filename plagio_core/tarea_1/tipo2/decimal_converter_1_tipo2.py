def base_converter(valor):
    bin_str = bin(valor)[2:]
    oct_str = oct(valor)[2:]
    hex_str = hex(valor)[2:].upper()

    print(f"DEC: {valor}")
    print(f"BIN: {bin_str}")
    print(f"OCT: {oct_str}")
    print(f"HEX: {hex_str}")

def inicio():
    print("Convertidor de número decimal")
    try:
        entrada = int(input("Ingresa un número entero positivo: "))
        if entrada < 0:
            print("Solo se permiten números positivos.")
            return
        base_converter(entrada)
    except ValueError:
        print("Error: valor no válido.")

inicio()

