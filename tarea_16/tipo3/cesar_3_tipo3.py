class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self):
        n = input("Nombre: ")
        t = input("Tel: ")
        self.contactos.append(Contacto(n, t))

    def buscar(self):
        n = input("Buscar: ")
        encontrados = [c for c in self.contactos if c.nombre == n]
        if encontrados:
            print(f"{n}: {encontrados[0].telefono}")
        else:
            print("No existe.")

    def mostrar(self):
        if not self.contactos:
            print("Agenda vacía.")
        for c in self.contactos:
            print(f"{c.nombre} - {c.telefono}")

a = Agenda()
while True:
    print("1. Agregar\n2. Buscar\n3. Mostrar\n4. Salir")
    opc = input("Opción: ")
    if opc == "1": a.agregar()
    elif opc == "2": a.buscar()
    elif opc == "3": a.mostrar()
    elif opc == "4": break

