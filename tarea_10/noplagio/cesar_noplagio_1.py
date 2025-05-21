def construir_tabla(shift):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    desplazado = alfabeto[shift:] + alfabeto[:shift]
    return str.maketrans(alfabeto + alfabeto.upper(), desplazado + desplazado.upper())

def cifrar(mensaje, paso):
    tabla = construir_tabla(paso)
    return mensaje.translate(tabla)

def main():
    texto = input("Mensaje: ")
    clave = int(input("Desplazamiento: "))
    modo = input("(C)ifrar / (D)escifrar: ").lower()
    if modo == 'd':
        clave = -clave
    print("Resultado:", cifrar(texto, clave))

main()

