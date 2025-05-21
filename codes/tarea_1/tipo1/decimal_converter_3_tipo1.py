def main():
    print("== Conversor de Decimal a Otras Bases ==")
    try:
        numero = int(input("Número decimal: "))
        if numero < 0:
            print("Solo se permiten valores positivos.")
            return

        print("Resultados:")
        print("Binario     => {:b}".format(numero))
        print("Octal       => {:o}".format(numero))
        print("Hexadecimal => {:X}".format(numero))
    except ValueError:
        print("Debes ingresar un número entero.")

if __name__ == "__main__":
    main()