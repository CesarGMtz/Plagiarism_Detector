def mostrar_menu():
    print("\nAGENDA")
    print("1. Añadir")
    print("2. Buscar")
    print("3. Listar")
    print("4. Salir")

def añadir_contacto(agenda):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    if nombre in agenda:
        print("Ya existe. Se actualiza.")
    agenda[nombre] = numero

def buscar(agenda):
    buscar = input("Nombre a buscar: ")
    if buscar in agenda:
        print(f"{buscar}: {agenda[buscar]}")
    else:
        print("No existe.")

def listar(agenda):
    for nom in sorted(agenda):
        print(f"{nom}: {agenda[nom]}")

agenda = {}
while True:
    mostrar_menu()
    opc = input("Opción: ")
    if opc == "1":
        añadir_contacto(agenda)
    elif opc == "2":
        buscar(agenda)
    elif opc == "3":
        listar(agenda)
    elif opc == "4":
        break

