agenda = {}

def mostrar_menu():
    print("\nAGENDA DE CONTACTOS")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Eliminar")
    print("4. Salir")

def añadir():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    if nombre in agenda:
        print("Ya existe.")
    else:
        agenda[nombre] = telefono
        print("Añadido.")

def ver():
    if not agenda:
        print("No hay contactos.")
    else:
        for nombre, tel in agenda.items():
            print(f"{nombre}: {tel}")

def eliminar():
    nombre = input("Eliminar: ")
    if agenda.pop(nombre, None):
        print("Eliminado.")
    else:
        print("No se encontró.")

def ejecutar():
    while True:
        mostrar_menu()
        op = input("Elige opción: ")
        if op == "1":
            añadir()
        elif op == "2":
            ver()
        elif op == "3":
            eliminar()
        elif op == "4":
            break
        else:
            print("Opción inválida.")

ejecutar()

