def cifrado_cesar(texto, paso):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            codificada = chr((ord(letra) - base + paso) % 26 + base)
            resultado += codificada
        else:
            resultado += letra
    return resultado

def solicitar_texto():
    return input("Texto a cifrar: ")

def solicitar_paso():
    try:
        return int(input("Paso (número de desplazamiento): "))
    except ValueError:
        print("Paso inválido.")
        return 3  # valor por defecto

def ejecutar():
    while True:
        texto = solicitar_texto()
        paso = solicitar_paso()
        cifrado = cifrado_cesar(texto, paso)
        print("Resultado:", cifrado)
        if input("¿Deseas salir? (s/n): ").lower() == 's':
            break

ejecutar()

