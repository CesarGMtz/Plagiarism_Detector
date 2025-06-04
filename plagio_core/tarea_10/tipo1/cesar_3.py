def validar(texto):
    return ''.join(c for c in texto if c.isprintable())

def cifrado_cesar(texto, shift):
    texto = validar(texto)
    return ''.join(
        chr((ord(c) - base + shift) % 26 + base) if c.isalpha() else c
        for c in texto
        for base in [ord('A') if c.isupper() else ord('a')] if c.isalpha()
    )

def interactivo():
    t = input("Texto: ")
    s = int(input("Desplazamiento: "))
    m = input("(C)ifrar o (D)escifrar?: ").strip().lower()
    s = -s if m == 'd' else s
    print("Resultado:", cifrado_cesar(t, s))

interactivo()

