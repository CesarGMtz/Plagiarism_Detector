def cesar_codificador(texto, clave, modo="cifrar"):
    if modo == "descifrar":
        clave = -clave
    salida = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nuevo = chr((ord(char) - base + clave) % 26 + base)
            salida += nuevo
        else:
            salida += char
    return salida

msg = input("Mensaje: ")
key = int(input("Desplazamiento: "))
modo = input("¿C o D?: ").strip().lower()

tipo = "cifrar" if modo == 'c' else "descifrar"
print("Texto resultante:", cesar_codificador(msg, key, tipo))

