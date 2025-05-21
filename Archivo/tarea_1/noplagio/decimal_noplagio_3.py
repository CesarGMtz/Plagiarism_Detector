def solicitar_decimal():
    while True:
        entrada = input("Escribe un número en base 10: ")
        if entrada.isdigit():
            return int(entrada)
        print("Entrada inválida. Intenta con un número entero positivo.")

def conversor_base(decimal):
    bases = {
        "Binario": format(decimal, 'b'),
        "Octal": format(decimal, 'o'),
        "Hexadecimal": format(decimal, 'X')
    }
    return bases

def mostrar_conversiones(bases_dict):
    print("\nResultados de la conversión:")
    for nombre, valor in bases_dict.items():
        print(f"{nombre}: {valor}")

def ejecutar():
    print("== Conversor de Decimal a otras Bases ==")
    numero = solicitar_decimal()
    resultado = conversor_base(numero)
    mostrar_conversiones(resultado)

if __name__ == "__main__":
    ejecutar()
