def menu():
    print("1) Nuevo contacto")
    print("2) Buscar")
    print("3) Ver todo")
    print("4) Salir")

def agregar(dic):
    n = input("Nombre: ")
    t = input("Tel: ")
    dic[n] = t
    print("✓ Guardado")

def buscar(dic):
    q = input("Nombre a buscar: ")
    print(f"{q}: {dic.get(q, 'No encontrado')}")

def ver(dic):
    if dic:
        [print(f"{k} → {v}") for k,v in dic.items()]
    else:
        print("Sin contactos.")

contactos = {}
while True:
    menu()
    o = input("Elige: ")
    if o == "1": agregar(contactos)
    elif o == "2": buscar(contactos)
    elif o == "3": ver(contactos)
    elif o == "4": break

