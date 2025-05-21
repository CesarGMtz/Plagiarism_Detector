def menu():
    print("Agenda Telefónica")
    print("1. Alta contacto")
    print("2. Búsqueda")
    print("3. Ver agenda")
    print("4. Salir")

def alta(dic):
    n = input("Nombre del contacto: ")
    t = input("Teléfono: ")
    if n in dic:
        print("Contacto ya existe, reemplazado.")
    dic[n] = t

def consulta(dic):
    c = input("¿A quién buscas?: ")
    if c in dic:
        print(f"{c} tiene el número {dic[c]}")
    else:
        print("No se encontró.")

def imprimir(dic):
    for k in sorted(dic):
        print(f"{k} -> {dic[k]}")

mis_contactos = {}

while True:
    menu()
    sel = input("Selecciona: ")
    if sel == "1":
        alta(mis_contactos)
    elif sel == "2":
        consulta(mis_contactos)
    elif sel == "3":
        imprimir(mis_contactos)
    elif sel == "4":
        break

