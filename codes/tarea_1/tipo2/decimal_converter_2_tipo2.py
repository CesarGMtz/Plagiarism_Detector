def obtener_conversiones(n):
    return {
        'Bin': lambda v: bin(v)[2:],
        'Oct': lambda v: oct(v)[2:],
        'Hex': lambda v: hex(v)[2:].upper()
    }

def mostrar_todo(n):
    conversiones = obtener_conversiones(n)
    print(f"Convertir el número: {n}")
    for clave in conversiones:
        resultado = conversiones[clave](n)
        print(f"{clave}: {resultado}")

def inicio():
    print("Inicio del conversor")
    try:
        dato = int(input("Número: "))
        if dato >= 0:
            mostrar_todo(dato)
        else:
            print("Debe ser positivo.")
    except:
        print("Dato inválido")

inicio()