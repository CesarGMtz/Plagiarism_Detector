agenda = {}

def acciones(op):
    if op == "1":
        nombre = input("Nombre: ")
        tel = input("Teléfono: ")
        agenda[nombre] = tel
        print("Añadido.")
    elif op == "2":
        n = input("Buscar: ")
        print(f"{n}: {agenda[n]}" if n in agenda else "No existe.")
    elif op == "3":
        if agenda:
            for k, v in agenda.items():
                print(f"{k} - {v}")
        else:
            print("Agenda vacía.")
    elif op != "4":
        print("Inválido.")

def menu():
    print("1. Agregar\n2. Buscar\n3. Ver\n4. Salir")

opcion = ""
while opcion != "4":
    menu()
    opcion = input("Opción: ")
    acciones(opcion)

