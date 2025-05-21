def mostrar_opciones():
    print("\nBloc de Notas Simple")
    print("1. Añadir nota")
    print("2. Listar notas")
    print("3. Quitar nota")
    print("4. Salir")

def añadir(lista):
    nueva = input("Nueva nota: ")
    lista.append(nueva)
    print("Nota añadida.")

def listar(lista):
    if not lista:
        print("Vacío.")
    else:
        for i, n in enumerate(lista, 1):
            print(f"{i}. {n}")

def quitar(lista):
    listar(lista)
    if lista:
        try:
            pos = int(input("Número de nota a quitar: ")) - 1
            if 0 <= pos < len(lista):
                lista.pop(pos)
                print("Eliminada.")
            else:
                print("Inválido.")
        except ValueError:
            print("Entrada errónea.")

def principal():
    notas = []
    while True:
        mostrar_opciones()
        op = input("Selecciona: ")
        if op == '1':
            añadir(notas)
        elif op == '2':
            listar(notas)
        elif op == '3':
            quitar(notas)
        elif op == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

principal()

