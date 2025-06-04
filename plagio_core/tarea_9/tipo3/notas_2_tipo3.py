def menu():
    print("\n*** Menú de Notas ***")
    print("1. Escribir nota")
    print("2. Ver notas")
    print("3. Eliminar todas")
    print("4. Salir")

def nueva_nota(notas):
    texto = input("Nueva nota: ")
    notas.append(texto)
    print("Guardada.")

def ver_notas(notas):
    if not notas:
        print("Sin notas.")
        return
    print("--- Tus Notas ---")
    for i, n in enumerate(notas, 1):
        print(f"{i}) {n}")

def eliminar_todas(notas):
    confirmacion = input("¿Seguro que quieres borrar todas las notas? (s/n): ")
    if confirmacion.lower() == "s":
        notas.clear()
        print("Notas eliminadas.")
    else:
        print("Acción cancelada.")

def iniciar():
    notas = []
    while True:
        menu()
        opcion = input("Opción: ")
        if opcion == "1":
            nueva_nota(notas)
        elif opcion == "2":
            ver_notas(notas)
        elif opcion == "3":
            eliminar_todas(notas)
        elif opcion == "4":
            break
        else:
            print("Inválido.")

iniciar()

