from datetime import datetime

notas = []

def agregar():
    contenido = input("Nota nueva: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    notas.append([fecha, contenido])

def ver():
    for i, nota in enumerate(notas):
        print(f"{i+1}) [{nota[0]}] {nota[1]}")

def eliminar():
    ver()
    try:
        x = int(input("Eliminar número: ")) - 1
        if 0 <= x < len(notas):
            notas.pop(x)
    except:
        print("Entrada inválida.")

def interfaz():
    while True:
        print("\n--- Bloc de notas ---")
        op = input("1.Agregar 2.Ver 3.Borrar 4.Salir > ")
        if op == '1':
            agregar()
        elif op == '2':
            ver()
        elif op == '3':
            eliminar()
        elif op == '4':
            break

interfaz()

