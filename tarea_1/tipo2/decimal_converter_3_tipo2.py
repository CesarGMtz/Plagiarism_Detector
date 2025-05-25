def ejecutar():
    print("== Conversión de decimal a bin/oct/hex ==")
    try:
        valor = int(input("Introduce un número: "))
        if valor < 0:
            print("No se permiten negativos.")
            return

        print("=== Resultado ===")
        print("BIN:", format(valor, "b"))
        print("OCT:", format(valor, "o"))
        print("HEX:", format(valor, "X"))
    except ValueError:
        print("Entrada inválida. Usa un número entero.")

if __name__ == "__main__":
    ejecutar()

