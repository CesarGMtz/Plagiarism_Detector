agenda = {}

def añadir_contacto():
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        print("Ya existe.")
    else:
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
        print("Guardado.")

def buscar_contacto():
    nombre = input("Buscar nombre: ")
    telefono = agenda.get(nombre)
    if telefono:
        print(f"{nombre}: {telefono}")
    else:
        print("No encontrado.")

def eliminar_contacto():
    nombre = input("Eliminar nombre: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Eliminado.")
    else:
        print("No existe.")

def menu_principal():
    while True:
        print("\n1. Añadir\n2. Buscar\n3. Eliminar\n4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

menu_principal()

