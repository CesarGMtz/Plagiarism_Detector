agenda = {}

def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1) Agregar nuevo")
    print("2) Buscar contacto")
    print("3) Ver todos")
    print("4) Salir")

def agregar():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print("Contacto guardado.")

def buscar():
    nombre = input("Nombre a buscar: ")
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("No encontrado.")

def ver_todos():
    if not agenda:
        print("Agenda vacía.")
    else:
        for nombre, tel in agenda.items():
            print(f"{nombre}: {tel}")

def ejecutar():
    while True:
        mostrar_menu()
        op = input("Elige una opción: ")
        if op == "1":
            agregar()
        elif op == "2":
            buscar()
        elif op == "3":
            ver_todos()
        elif op == "4":
            break
        else:
            print("Opción inválida.")

ejecutar()

