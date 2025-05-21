contactos = {}

def opciones():
    print("1. Añadir")
    print("2. Buscar")
    print("3. Ver todos")
    print("4. Cerrar")

def añadir(diccionario):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    diccionario[nombre] = numero

def buscar_nombre(diccionario):
    nombre = input("Nombre a buscar: ")
    if nombre in diccionario:
        print(nombre, ":", diccionario[nombre])
    else:
        print("No hallado.")

def mostrar_todos(diccionario):
    if diccionario != {}:
        for clave in diccionario:
            print(f"{clave} => {diccionario[clave]}")
    else:
        print("Vacío.")

while True:
    opciones()
    eleccion = input("Ingresa opción: ")
    if eleccion == "1": añadir(contactos)
    elif eleccion == "2": buscar_nombre(contactos)
    elif eleccion == "3": mostrar_todos(contactos)
    elif eleccion == "4": break

