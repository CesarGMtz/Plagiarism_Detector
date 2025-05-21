import unicodedata

def normalizar(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn')

def convertir(msg, k, descifrar=False):
    k = -k if descifrar else k
    res = ""
    for l in normalizar(msg):
        if l.isalpha():
            base = ord('a') if l.islower() else ord('A')
            res += chr((ord(l) - base + k) % 26 + base)
        else:
            res += l
    return res

texto = input("Mensaje: ")
clave = int(input("Clave: "))
modo = input("Modo (c/d): ").lower()
print("Salida:", convertir(texto, clave, descifrar=(modo == 'd')))

