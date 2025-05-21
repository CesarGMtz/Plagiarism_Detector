def decimal_a_binario(numero):
    return bin(numero)[2:]

def decimal_a_octal(numero):
    return oct(numero)[2:]

def decimal_a_hexadecimal(numero):
    return hex(numero)[2:]

def mostrar_conversiones(n):
    print(f"Binario: {decimal_a_binario(n)}")
    print(f"Octal: {decimal_a_octal(n)}")
    print(f"Hexadecimal: {decimal_a_hexadecimal(n)}")

def flujo_principal():
    while True:
        try:
            entrada = input("Introduce un número decimal (o 'salir'): ")
            if entrada.lower() == "salir":
                break
            numero = int(entrada)
            mostrar_conversiones(numero)
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

flujo_principal()

