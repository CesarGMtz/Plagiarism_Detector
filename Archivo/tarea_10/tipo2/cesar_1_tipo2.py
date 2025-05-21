def cesar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            nueva = chr((ord(c) - base + desplazamiento) % 26 + base)
            resultado += nueva
        else:
            resultado += c
    return resultado

def iniciar():
    while True:
        accion = input("\nEscribe 'cifrar', 'descifrar' o 'salir': ").lower()
        if accion == 'salir':
            break
        if accion in ['cifrar', 'descifrar']:
            texto = input("Mensaje: ")
            valor = int(input("Desplazamiento: "))
            valor = -valor if accion == 'descifrar' else valor
            print("Resultado:", cesar(texto, valor))
        else:
            print("Comando no reconocido.")

iniciar()

