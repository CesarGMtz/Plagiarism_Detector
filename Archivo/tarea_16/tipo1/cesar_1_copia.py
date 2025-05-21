agenda_contactos = {}

def nuevo_contacto():
    nom = input("Nombre: ")
    tel = input("Teléfono: ")
    agenda_contactos[nom] = tel
    print("Contacto guardado.")

def ver_contacto():
    nom = input("Buscar: ")
    if nom in agenda_contactos:
        print(nom + ": " + agenda_contactos[nom])
    else:
        print("No encontrado.")

def lista_contactos():
    if len(agenda_contactos) == 0:
        print("Vacía.")
    else:
        for c in agenda_contactos:
            print(c + ": " + agenda_contactos[c])

while True:
    print("1.Agregar 2.Buscar 3.Mostrar 4.Salir")
    op = input("Elige: ")
    if op == "1":
        nuevo_contacto()
    elif op == "2":
        ver_contacto()
    elif op == "3":
        lista_contactos()
    elif op == "4":
        break

