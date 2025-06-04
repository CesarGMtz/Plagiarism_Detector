def mostrar_menu():
    print("\n=== Gestor de Notas ===")
    print("1. Crear nota")
    print("2. Ver notas")
    print("3. Quitar nota")
    print("4. Salir")

def crear_nota(registro, actual):
    contenido = input("Nueva nota: ")
    registro[actual] = contenido
    print(f"Guardado como nota #{actual}")
    return actual + 1

def ver_notas(registro):
    if not registro:
        print("No hay notas disponibles.")
    else:
        for id, texto in registro.items():
            print(f"[{id}] {texto}")

def quitar_nota(registro):
    ver_notas(registro)
    try:
        objetivo = int(input("ID a quitar: "))
        if objetivo in registro:
            del registro[objetivo]
            print("Nota eliminada.")
        else:
            print("ID no encontrado.")
    except ValueError:
        print("Dato no válido.")

def iniciar_sesion():
    base = {}
    contador = 1
    while True:
        mostrar_menu()
        eleccion = input("Selecciona opción: ")
        if eleccion == '1':
            contador = crear_nota(base, contador)
        elif eleccion == '2':
            ver_notas(base)
        elif eleccion == '3':
            quitar_nota(base)
        elif eleccion == '4':
            print("Cerrando notas...")
            break
        else:
            print("Opción inválida.")

iniciar_sesion()

