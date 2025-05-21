notas = []

def menu():
    return input("\n[+] Opciones: [1] Añadir  [2] Ver  [3] Borrar  [4] Salir\n> ")

def añadir():
    texto = input("Contenido de nota: ")
    confirm = input("¿Guardar? (s/n): ")
    if confirm.lower() == 's':
        notas.append(texto)
        print("Nota guardada.")

def ver():
    if notas:
        print("\nTus notas:")
        for idx, n in enumerate(notas, 1):
            print(f"{idx}. {n}")
    else:
        print("No hay notas registradas.")

def borrar():
    ver()
    try:
        pos = int(input("Número a eliminar: ")) - 1
        if 0 <= pos < len(notas):
            del notas[pos]
            print("Eliminada.")
    except:
        print("Error al eliminar.")

while True:
    eleccion = menu()
    if eleccion == '1':
        añadir()
    elif eleccion == '2':
        ver()
    elif eleccion == '3':
        borrar()
    elif eleccion == '4':
        break

