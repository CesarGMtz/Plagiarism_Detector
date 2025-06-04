def menu_agenda():
    print("\nAGENDA PERSONAL")
    print("1. Nuevo contacto")
    print("2. Buscar contacto")
    print("3. Ver agenda")
    print("4. Salir")

def guardar_contacto(libro):
    nombre = input("Nombre del contacto: ")
    tel = input("Teléfono: ")
    if nombre in libro:
        print("Contacto ya existente. Actualizado.")
    libro[nombre] = tel

def consultar_contacto(libro):
    clave = input("Buscar nombre: ")
    if clave in libro:
        print(f"{clave}: {libro[clave]}")
    else:
        print("No está registrado.")

def ver_contactos(libro):
    for clave in sorted(libro):
        print(f"{clave} → {libro[clave]}")

agenda = {}
while True:
    menu_agenda()
    eleccion = input("Elige una opción: ")
    if eleccion == "1":
        guardar_contacto(agenda)
    elif eleccion == "2":
        consultar_contacto(agenda)
    elif eleccion == "3":
        ver_contactos(agenda)
    elif eleccion == "4":
        break

