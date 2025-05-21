def mostrar_menu():
    print("\nEditor de Notas")
    print("1. Agregar nota")
    print("2. Ver notas")
    print("3. Borrar nota")
    print("4. Salir")

def agregar(notas):
    texto = input("Escribe la nueva nota: ")
    notas.append(texto)
    print("Nota guardada.")

def ver(notas):
    if not notas:
        print("No hay notas.")
    else:
        for i, nota in enumerate(notas, 1):
            print(f"{i}. {nota}")

def borrar(notas):
    ver(notas)
    if notas:
        try:
            indice = int(input("Número de nota a borrar: ")) - 1
            if 0 <= indice < len(notas):
                eliminada = notas.pop(indice)
                print(f"Nota eliminada: {eliminada}")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada no válida.")

def main():
    notas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar(notas)
        elif opcion == '2':
            ver(notas)
        elif opcion == '3':
            borrar(notas)
        elif opcion == '4':
            print("Saliendo del editor...")
            break
        else:
            print("Opción inválida.")

main()

