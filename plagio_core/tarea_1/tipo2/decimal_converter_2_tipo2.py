def obtener_bases(valor):
    return {
        'bin': lambda x: bin(x)[2:],
        'oct': lambda x: oct(x)[2:],
        'hex': lambda x: hex(x)[2:].upper()
    }

def imprimir_bases(numero):
    mapas = obtener_bases(numero)
    print(f"DEC: {numero}")
    for clave, fx in mapas.items():
        print(f"{clave.upper()}: {fx(numero)}")

def iniciar():
    print("Conversión desde decimal")
    try:
        dato = int(input("Número: "))
        if dato >= 0:
            imprimir_bases(dato)
        else:
            print("No se permiten negativos.")
    except:
        print("Dato inválido.")

iniciar()

