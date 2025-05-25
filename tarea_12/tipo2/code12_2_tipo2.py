import random
import string

def generar_clave(segura=True, tamaño=12):
    caracteres = string.ascii_letters + string.digits
    if segura:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamaño))

def contiene_repetidos(conjunto):
    return len(conjunto) != len(set(conjunto))

def crear_lista_segura(cantidad, tamaño=12):
    claves = []
    while len(claves) < cantidad:
        nueva = generar_clave(True, tamaño)
        if nueva not in claves:
            claves.append(nueva)
    return claves

def iniciar():
    cantidad = int(input("¿Cuántas claves generar?: "))
    claves = crear_lista_segura(cantidad)
    if contiene_repetidos(claves):
        print("Hay duplicados.")
    else:
        print("Todas son únicas.")
    print("\nContraseñas generadas:")
    for clave in claves:
        print(clave)

iniciar()

