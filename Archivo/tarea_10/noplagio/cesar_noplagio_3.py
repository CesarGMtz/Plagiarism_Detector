def cifrar_palabra(palabra, salto):
    resultado = ""
    for l in palabra:
        if l.isalpha():
            base = ord('A') if l.isupper() else ord('a')
            resultado += chr((ord(l) - base + salto) % 26 + base)
        else:
            resultado += l
    return resultado

def procesar_frase(frase, paso):
    return ' '.join([cifrar_palabra(p, paso) for p in frase.split()])

mensaje = input("Frase: ")
clave = int(input("Shift: "))
modo = input("¿Descifrar? (s/n): ").lower()
if modo == 's':
    clave = -clave
print("Resultado:", procesar_frase(mensaje, clave))

