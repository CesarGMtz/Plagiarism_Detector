def menu():
    print("== CONVERSOR DECIMAL A BASES ==")
    print("Escribe un número decimal para convertirlo.")
    print("Escribe 'salir' para terminar.")

def obtener_entrada():
    return input("Número: ")

def mostrar_resultado(n):
    print(f"→ Binario     : {bin(n)[2:]}")
    print(f"→ Octal       : {oct(n)[2:]}")
    print(f"→ Hexadecimal : {hex(n)[2:]}")

def proceso():
    while True:
        entrada = obtener_entrada()
        if entrada.strip().lower() == 'salir':
            break
        try:
            numero = int(entrada)
            mostrar_resultado(numero)
        except ValueError:
            print("Por favor ingresa un número válido.")

def main():
    menu()
    proceso()

main()

