def encriptar(mensaje, paso):
    resultado = ""
    for letra in mensaje:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nueva_letra = chr((ord(letra) - base + paso) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

def desencriptar(mensaje, paso):
    return encriptar(mensaje, -paso)

def mostrar_menu():
    print("\nMENÚ CÉSAR")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        eleccion = input("Elige opción: ")
        if eleccion == '1':
            texto = input("Texto a encriptar: ")
            paso = int(input("Clave numérica: "))
            print("Resultado:", encriptar(texto, paso))
        elif eleccion == '2':
            texto = input("Texto a desencriptar: ")
            paso = int(input("Clave numérica: "))
            print("Resultado:", desencriptar(texto, paso))
        elif eleccion == '3':
            break
        else:
            print("Opción inválida.")

ejecutar()

