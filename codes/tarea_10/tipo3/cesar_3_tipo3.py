def solo_printable(texto):
    return ''.join(c for c in texto if c.isprintable())

def cifrar(texto, desplazamiento):
    texto = solo_printable(texto)
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

def descifrar(texto, paso):
    return cifrar(texto, -paso)

def entrada_modo():
    m = input("Modo (cifrar/descifrar): ").strip().lower()
    return m if m in ["cifrar", "descifrar"] else "cifrar"

def ejecutar():
    while True:
        modo = entrada_modo()
        texto = input("Texto: ")
        try:
            paso = int(input("Paso: "))
        except:
            paso = 3
        if modo == "cifrar":
            print("Cifrado:", cifrar(texto, paso))
        else:
            print("Descifrado:", descifrar(texto, paso))
        if input("¿Finalizar? (s/n): ").lower() == 's':
            break

ejecutar()

