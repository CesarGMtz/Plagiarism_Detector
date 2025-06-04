def cifrado_cesar(cadena, clave, accion="cifrar"):
    if accion == "descifrar":
        clave = -clave
    salida = ""
    for letra in cadena:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nuevo = chr((ord(letra) - base + clave) % 26 + base)
            salida += nuevo
        else:
            salida += letra
    return salida

entrada = input("Ingresa el texto: ")
salto = int(input("Ingresa la clave: "))
opcion = input("¿Deseas cifrar (C) o descifrar (D)?: ").lower()
modo = "cifrar" if opcion == "c" else "descifrar"

print("Texto procesado:", cifrado_cesar(entrada, salto, modo))

