import random
import string

def menu():
    print("1. Generar contraseña")
    print("2. Ver todas")
    print("3. Salir")

def generar_una(longitud):
    base = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(base, k=longitud))

def main():
    almacen = {}
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Nombre para la contraseña: ")
            if nombre in almacen:
                print("Ya existe un registro con ese nombre.")
                continue
            pwd = generar_una(12)
            almacen[nombre] = pwd
            print(f"Contraseña para {nombre}: {pwd}")
        elif opcion == "2":
            for clave, valor in almacen.items():
                print(f"{clave}: {valor}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

main()

