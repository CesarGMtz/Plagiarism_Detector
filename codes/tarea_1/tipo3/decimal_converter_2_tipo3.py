def convertir_decimal(numero):
    conversiones = {
        'binario': bin(numero)[2:],
        'octal': oct(numero)[2:],
        'hexadecimal': hex(numero)[2:]
    }
    return conversiones

def imprimir_conversiones(diccionario):
    for base, valor in diccionario.items():
        print(f"{base.capitalize()}: {valor}")

def ejecutar():
    continuar = True
    while continuar:
        entrada = input("Número decimal (o 'x' para salir): ")
        if entrada.strip().lower() == 'x':
            continuar = False
        elif entrada.isdigit():
            resultado = convertir_decimal(int(entrada))
            imprimir_conversiones(resultado)
        else:
            print("Entrada no válida.")

ejecutar()

