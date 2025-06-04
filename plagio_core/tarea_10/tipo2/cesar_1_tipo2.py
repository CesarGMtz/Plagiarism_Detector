def encriptar(cadena, shift):
    resultado = ""
    for char in cadena:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cifrado = chr((ord(char) - base + shift) % 26 + base)
            resultado += cifrado
        else:
            resultado += char
    return resultado

def desencriptar(cadena, shift):
    return encriptar(cadena, -shift)

def mostrar_menu():
    print("\n== CIFRADO CÉSAR ==")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        eleccion = input("Selecciona una opción: ")
        if eleccion == '1':
            txt = input("Texto a encriptar: ")
            desplazamiento = int(input("Desplazamiento: "))
            print("Resultado:", encriptar(txt, desplazamiento))
        elif eleccion == '2':
            txt = input("Texto a desencriptar: ")
            desplazamiento = int(input("Desplazamiento: "))
            print("Resultado:", desencriptar(txt, desplazamiento))
        elif eleccion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

ejecutar()

