import random
import string

def crear_contraseña(segura=True, longitud=12):
    base = string.ascii_letters + string.digits
    if segura:
        base += string.punctuation
    return ''.join(random.choice(base) for _ in range(longitud))

def hay_duplicados(lista):
    return len(lista) != len(set(lista))

def generar_conjunto_seguro(n, longitud=12):
    lista = []
    while len(lista) < n:
        nueva = crear_contraseña(True, longitud)
        if nueva not in lista:
            lista.append(nueva)
    return lista

def main():
    total = int(input("Cantidad de contraseñas: "))
    contraseñas = generar_conjunto_seguro(total)
    if hay_duplicados(contraseñas):
        print("Se encontraron duplicados.")
    else:
        print("Todas las contraseñas son únicas.")
    print("\nListado:")
    for c in contraseñas:
        print(c)

main()

