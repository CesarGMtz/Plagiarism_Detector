def menu():
    print("\nBloc de Notas")
    print("1. Nueva nota")
    print("2. Ver todas")
    print("3. Eliminar una")
    print("4. Cerrar")

def nueva(notas):
    nueva_nota = input("Escribe tu nota: ")
    notas.append(nueva_nota)
    print("Nota añadida.")

def listar(notas):
    if not notas:
        print("Sin notas registradas.")
    else:
        for idx, contenido in enumerate(notas, start=1):
            print(f"{idx}. {contenido}")

def eliminar(notas):
    listar(notas)
    if notas:
        try:
            pos = int(input("¿Qué número de nota eliminar? ")) - 1
            if 0 <= pos < len(notas):
                removida = notas.pop(pos)
                print(f"Nota eliminada: {removida}")
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada no válida.")

def iniciar():
    lista = []
    while True:
        menu()
        eleccion = input("Elige una opción: ")
        if eleccion == '1':
            nueva(lista)
        elif eleccion == '2':
            listar(lista)
        elif eleccion == '3':
            eliminar(lista)
        elif eleccion == '4':
            print("Cerrando aplicación de notas...")
            break
        else:
            print("Opción incorrecta.")

iniciar()

