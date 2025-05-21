agenda = {}

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print("Contacto agregado.")

def buscar_contacto():
    nombre = input("Buscar nombre: ")
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("No encontrado.")

def mostrar_contactos():
    if not agenda:
        print("Agenda vacía.")
    else:
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

while True:
    print("\n1. Agregar\n2. Buscar\n3. Mostrar\n4. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")

