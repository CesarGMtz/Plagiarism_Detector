def mostrar_menu():
    print("\n=== Editor de Notas ===")
    print("1. Agregar nota")
    print("2. Mostrar notas")
    print("3. Salir")

def agregar_nota(lista):
    nota = input("Escribe tu nota: ")
    lista.append(nota)
    print("Nota agregada.")

def mostrar_notas(lista):
    if not lista:
        print("No hay notas registradas.")
    else:
        print("Notas guardadas:")
        for i, n in enumerate(lista, 1):
            print(f"{i}. {n}")

def bucle_principal():
    notas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_nota(notas)
        elif opcion == "2":
            mostrar_notas(notas)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

bucle_principal()

