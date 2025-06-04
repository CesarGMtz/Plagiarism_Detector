def mostrar_menu():
    print("Agenda Simple")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Salir")

def agregar(lista):
    c = {"nombre": input("Nombre: "), "tel": input("Teléfono: ")}
    lista.append(c)

def buscar(lista):
    nombre = input("Buscar nombre: ")
    for c in lista:
        if c["nombre"] == nombre:
            print(f"{c['nombre']} - {c['tel']}")
            return
    print("No encontrado.")

def listar(lista):
    for c in lista:
        print(f"{c['nombre']}: {c['tel']}")

def main():
    contactos = []
    while True:
        mostrar_menu()
        op = input("Opción: ")
        if op == "1": agregar(contactos)
        elif op == "2": buscar(contactos)
        elif op == "3": listar(contactos)
        elif op == "4": break

main()

