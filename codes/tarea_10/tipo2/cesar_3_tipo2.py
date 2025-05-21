def cesar(texto, shift):
    salida = ""
    for l in texto:
        if l.isalpha():
            base = ord('A') if l.isupper() else ord('a')
            nueva = chr((ord(l) - base + shift) % 26 + base)
            salida += nueva
        else:
            salida += l
    return salida

def consola():
    comandos = {
        '1': lambda t, s: cesar(t, s),
        '2': lambda t, s: cesar(t, -s)
    }

    while True:
        print("\n1. Cifrar\n2. Descifrar\n3. Salir")
        op = input("Opción: ")
        if op == '3':
            break
        elif op in comandos:
            msg = input("Texto: ")
            key = int(input("Desplazamiento: "))
            print("Resultado:", comandos[op](msg, key))
        else:
            print("Inválido.")

consola()

