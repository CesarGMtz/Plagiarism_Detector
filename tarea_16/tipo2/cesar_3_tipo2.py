agenda = {}

def ejecutar_op(op):
    match op:
        case "1":
            nombre = input("Nombre nuevo: ")
            tel = input("Teléfono: ")
            if nombre in agenda:
                print("Actualizado.")
            agenda[nombre] = tel
        case "2":
            buscar = input("Buscar nombre: ")
            print(f"{buscar}: {agenda.get(buscar, 'No encontrado')}")
        case "3":
            print("Lista:")
            for k in sorted(agenda):
                print(k, ":", agenda[k])
        case _:
            print("Opción inválida")

def mostrar_menu():
    print("1.Añadir  2.Buscar  3.Ver todo  4.Salir")

while True:
    mostrar_menu()
    op = input("Opción: ")
    if op == "4":
        break
    ejecutar_op(op)

