def limpiar(texto):
    return ''.join(c for c in texto if c.isprintable())

def cesar(texto, paso):
    texto = limpiar(texto)
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            resultado += chr((ord(letra) - base + paso) % 26 + base)
        else:
            resultado += letra
    return resultado

def interfaz():
    entrada = input("Mensaje a procesar: ")
    shift = int(input("¿Cuántos lugares mover?: "))
    accion = input("¿Cifrar (C) o Descifrar (D)?: ").lower()
    shift = -shift if accion == 'd' else shift
    print("Mensaje convertido:", cesar(entrada, shift))

interfaz()

