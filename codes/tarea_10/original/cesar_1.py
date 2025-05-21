def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nueva = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado += nueva
        else:
            resultado += letra
    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

def menu():
    print("\nCIFRADOR CÉSAR")
    print("1. Cifrar")
    print("2. Descifrar")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            mensaje = input("Mensaje a cifrar: ")
            clave = int(input("Desplazamiento: "))
            print("Resultado:", cifrar(mensaje, clave))
        elif opcion == '2':
            mensaje = input("Mensaje a descifrar: ")
            clave = int(input("Desplazamiento: "))
            print("Resultado:", descifrar(mensaje, clave))
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

main()

