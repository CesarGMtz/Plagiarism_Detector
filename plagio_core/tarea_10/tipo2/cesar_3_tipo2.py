def limpiar(cadena):
    return ''.join(ch for ch in cadena if ch.isprintable())

def aplicar_cesar(cadena, paso):
    cadena = limpiar(cadena)
    return ''.join(
        chr((ord(ch) - base + paso) % 26 + base) if ch.isalpha() else ch
        for ch in cadena
        for base in [ord('A') if ch.isupper() else ord('a')] if ch.isalpha()
    )

def sesion():
    original = input("Introduce el mensaje: ")
    desplazamiento = int(input("Cantidad de desplazamiento: "))
    operacion = input("¿Cifrar (C) o Descifrar (D)?: ").lower()
    desplazamiento = -desplazamiento if operacion == 'd' else desplazamiento
    print("Texto final:", aplicar_cesar(original, desplazamiento))

sesion()

