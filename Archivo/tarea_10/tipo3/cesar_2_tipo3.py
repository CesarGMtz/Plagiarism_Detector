def transformar(texto, paso, modo="cifrar"):
    if modo == "descifrar":
        paso = -paso
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nueva = chr((ord(letra) - base + paso) % 26 + base)
            resultado += nueva
        else:
            resultado += letra
    return resultado

def leer_opcion():
    print("1. Cifrar\n2. Descifrar")
    eleccion = input("Elige: ")
    return "cifrar" if eleccion == "1" else "descifrar"

def interfaz():
    while True:
        modo = leer_opcion()
        texto = input("Texto: ")
        try:
            paso = int(input("Paso: "))
        except:
            paso = 3
        print("Resultado:", transformar(texto, paso, modo))
        if input("¿Salir? (s/n): ").lower() == 's':
            break

interfaz()

