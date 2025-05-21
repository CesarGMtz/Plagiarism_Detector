def iniciar():
    print(">>> DECIMAL a BIN / OCT / HEX <<<")
    try:
        d = int(input("Introduce un valor: "))
        if d < 0:
            print("No se permiten números negativos.")
            return

        print("Conversión:")
        print("Bin: " + bin(d)[2:])
        print("Oct: " + oct(d)[2:])
        print("Hex: " + hex(d)[2:].upper())
    except:
        print("Entrada incorrecta.")

iniciar()