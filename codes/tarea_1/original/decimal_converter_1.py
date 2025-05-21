def convertir_decimal(numero):
    binario = bin(numero)[2:]
    octal = oct(numero)[2:]
    hexadecimal = hex(numero)[2:].upper()

    print(f"Decimal: {numero}")
    print(f"Binario: {binario}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")

def main():
    print("Conversor de base")
    try:
        numero = int(input("Introduce un número decimal: "))
        if numero < 0:
            print("Por favor, introduce un número positivo.")
            return
        convertir_decimal(numero)
    except ValueError:
        print("Entrada inválida. Se esperaba un número entero.")

main()