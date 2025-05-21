def cesar(texto, paso, modo="cifrar"):
    if modo == "descifrar":
        paso = -paso
    resultado = ""
    for c in texto:
        if c.isalpha():
            inicio = ord('A') if c.isupper() else ord('a')
            nuevo = chr((ord(c) - inicio + paso) % 26 + inicio)
            resultado += nuevo
        else:
            resultado += c
    return resultado

mensaje = input("Texto: ")
desplazamiento = int(input("Clave César: "))

op = input("¿Cifrar (C) o Descifrar (D)?: ").lower()
modo = "cifrar" if op == 'c' else "descifrar"

print("Resultado:", cesar(mensaje, desplazamiento, modo))

