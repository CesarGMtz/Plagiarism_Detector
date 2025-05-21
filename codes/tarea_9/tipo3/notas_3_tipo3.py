import os

ARCHIVO = "notas.txt"

def cargar_notas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return [line.strip() for line in f]
    return []

def guardar_notas(notas):
    with open(ARCHIVO, "w") as f:
        for nota in notas:
            f.write(nota + "\n")

def añadir_nota(notas):
    nota = input("Escribe la nota: ")
    notas.append(nota)
    guardar_notas(notas)
    print("Nota guardada.")

def mostrar(notas):
    if notas:
        print("Notas registradas:")
        for i, n in enumerate(notas, 1):
            print(f"{i}. {n}")
    else:
        print("No hay notas.")

def menu():
    print("\n--- MENÚ DE NOTAS ---")
    print("1. Añadir nota")
    print("2. Ver notas")
    print("3. Salir")

def ejecutar():
    notas = cargar_notas()
    while True:
        menu()
        opcion = input("Opción: ")
        if opcion == "1":
            añadir_nota(notas)
        elif opcion == "2":
            mostrar(notas)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

ejecutar()

