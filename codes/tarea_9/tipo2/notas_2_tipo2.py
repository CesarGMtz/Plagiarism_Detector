def menu():
    print("\n--- GESTOR DE NOTAS ---")
    print("1. Crear nota")
    print("2. Listar notas")
    print("3. Quitar nota")
    print("4. Salir")

def crear(notas, contador):
    nota = input("Nota nueva: ")
    notas.append([contador, nota])
    return contador + 1

def listar(notas):
    for idn, contenido in notas:
        print(f"[{idn}] {contenido}")

def quitar(notas):
    listar(notas)
    try:
        eliminar = int(input("ID a quitar: "))
        notas[:] = [n for n in notas if n[0] != eliminar]
        print("Nota eliminada.")
    except:
        print("Error.")

def programa():
    lista = []
    contador = 1
    while True:
        menu()
        opcion = input("Opción: ")
        if opcion == '1':
            contador = crear(lista, contador)
        elif opcion == '2':
            listar(lista)
        elif opcion == '3':
            quitar(lista)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

programa()

