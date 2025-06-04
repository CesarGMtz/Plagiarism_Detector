libreta = {}

def nuevo_contacto():
    nombre = input("Nombre del contacto: ")
    numero = input("Número telefónico: ")
    libreta[nombre] = numero
    print("Contacto guardado.")

def buscar():
    clave = input("Nombre a buscar: ")
    if clave in libreta:
        print(f"{clave}: {libreta[clave]}")
    else:
        print("No encontrado.")

def ver_todos():
    if not libreta:
        print("No hay contactos registrados.")
    else:
        for persona, cel in libreta.items():
            print(f"{persona}: {cel}")

def menu():
    while True:
        print("\n1. Añadir\n2. Consultar\n3. Listar\n4. Salir")
        eleccion = input("Escoge una opción: ")
        if eleccion == "1":
            nuevo_contacto()
        elif eleccion == "2":
            buscar()
        elif eleccion == "3":
            ver_todos()
        elif eleccion == "4":
            break
        else:
            print("Opción no válida.")

menu()

