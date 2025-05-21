def menu():
    print("\n== Menú de Notas ==")
    print("1. Crear")
    print("2. Ver")
    print("3. Eliminar")
    print("4. Terminar")

def crear(notas, idn):
    nota = input("Ingrese nota: ")
    notas[idn] = nota
    print("Guardada.")
    return idn + 1

def ver(notas):
    if notas:
        for k, v in notas.items():
            print(f"[{k}] {v}")
    else:
        print("No hay notas.")

def eliminar(notas):
    ver(notas)
    try:
        clave = int(input("ID a borrar: "))
        if clave in notas:
            del notas[clave]
            print("Hecho.")
        else:
            print("No encontrada.")
    except:
        print("Error.")

def run():
    bloc = {}
    actual = 1
    while True:
        menu()
        eleccion = input("Elige opción: ")
        if eleccion == '1':
            actual = crear(bloc, actual)
        elif eleccion == '2':
            ver(bloc)
        elif eleccion == '3':
            eliminar(bloc)
        elif eleccion == '4':
            print("Cerrando...")
            break
        else:
            print("Inválido.")

run()

