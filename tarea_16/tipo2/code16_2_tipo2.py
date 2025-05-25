def mostrar_menu():
    print("1) Añadir contacto")
    print("2) Consultar contacto")
    print("3) Mostrar todos")
    print("4) Salir")

def añadir_contacto(diccionario):
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    diccionario[nombre] = telefono
    print("✔ Contacto añadido.")

def consultar(diccionario):
    nombre = input("¿Qué nombre buscas?: ")
    print(f"{nombre}: {diccionario.get(nombre, 'No registrado')}")

def mostrar_todos(diccionario):
    if diccionario:
        for nombre, tel in diccionario.items():
            print(f"{nombre} → {tel}")
    else:
        print("Agenda vacía.")

agenda = {}
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        añadir_contacto(agenda)
    elif opcion == "2":
        consultar(agenda)
    elif opcion == "3":
        mostrar_todos(agenda)
    elif opcion == "4":
        break

