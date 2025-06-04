def menu():
    print("\n=== Notas Interactivas ===")
    print("1. Nueva nota")
    print("2. Mostrar todas")
    print("3. Eliminar por ID")
    print("4. Salir")

def nueva(notas, contador):
    texto = input("Escribe tu nota: ")
    notas[contador] = texto
    print(f"Nota #{contador} guardada.")
    return contador + 1

def mostrar(notas):
    if not notas:
        print("No hay notas registradas.")
    else:
        for clave, nota in notas.items():
            print(f"[{clave}] {nota}")

def eliminar(notas):
    mostrar(notas)
    try:
        clave = int(input("ID a eliminar: "))
        if clave in notas:
            del notas[clave]
            print("Nota eliminada.")
        else:
            print("ID no encontrado.")
    except ValueError:
        print("Entrada inválida.")

def programa():
    notas = {}
    id_actual = 1
    while True:
        menu()
        opcion = input("Elige: ")
        if opcion == '1':
            id_actual = nueva(notas, id_actual)
        elif opcion == '2':
            mostrar(notas)
        elif opcion == '3':
            eliminar(notas)
        elif opcion == '4':
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

programa()

