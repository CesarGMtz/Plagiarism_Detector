def convertir(numero):
    return {
        'binario': lambda x: bin(x)[2:],
        'octal': lambda x: oct(x)[2:],
        'hex': lambda x: hex(x)[2:].upper()
    }

def mostrar_conversiones(num):
    funciones = convertir(num)
    print(f"Número decimal: {num}")
    for base, funcion in funciones.items():
        print(f"{base.capitalize()}: {funcion(num)}")

def main():
    print("Conversor Decimal a Binario/Octal/Hex")
    try:
        entrada = int(input("Ingresa un número: "))
        if entrada >= 0:
            mostrar_conversiones(entrada)
        else:
            print("Solo se permiten enteros positivos.")
    except:
        print("Entrada inválida.")

main()