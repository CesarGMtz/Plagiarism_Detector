def aplicar_cesar(cadena, paso, modo):
    if modo == 'd':
        paso = -paso
    final = ""
    for ch in cadena:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            final += chr((ord(ch) - base + paso) % 26 + base)
        else:
            final += ch
    return final

def main():
    print("== Cifrado César Simple ==")
    while True:
        texto = input("Texto: ")
        if not texto:
            break
        paso = int(input("Shift: "))
        modo = input("Modo (c=dato cifrado / d=dato claro): ")
        print(">>", aplicar_cesar(texto, paso, modo))

main()

