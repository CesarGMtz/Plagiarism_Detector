import json

def cargar_agenda():
    try:
        with open("agenda.json", "r") as f:
            return json.load(f)
    except:
        return {}

def guardar_agenda(agenda):
    with open("agenda.json", "w") as f:
        json.dump(agenda, f)

def main():
    agenda = cargar_agenda()
    while True:
        print("1.Guardar 2.Consultar 3.Ver todos 4.Salir")
        op = input("Elige: ")
        if op == "1":
            n = input("Nombre: ")
            t = input("Teléfono: ")
            agenda[n] = t
            guardar_agenda(agenda)
        elif op == "2":
            n = input("Buscar: ")
            print(agenda.get(n, "No registrado"))
        elif op == "3":
            print(json.dumps(agenda, indent=2))
        elif op == "4":
            break

main()

