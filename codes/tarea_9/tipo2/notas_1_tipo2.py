def mostrar_menu():
    print("\n📝 Menú de Notas")
    print("1. Añadir")
    print("2. Ver")
    print("3. Eliminar")
    print("4. Salir")

def agregar(lista):
    texto = input("Escribe tu nota: ")
    index = len(lista) + 1
    lista.append((index, texto))
    print(f"Nota #{index} añadida.")

def ver(lista):
    if not lista:
        print("No hay notas.")
    else:
        for idx, txt in lista:
            print(f"[{idx}] {txt}")

def eliminar(lista):
    ver(lista)
    if lista:
        try:
            eliminar_id = int(input("ID a eliminar: "))
            lista[:] = [(i, t) for i, t in lista if i != eliminar_id]
            print("Nota eliminada.")
        except:
            print("Entrada inválida.")

def main():
    notas = []
    while True:
        mostrar_menu()
        op = input("Selecciona: ")
        if op == '1':
            agregar(notas)
        elif op == '2':
            ver(notas)
        elif op == '3':
            eliminar(notas)
        elif op == '4':
            print("Saliendo.")
            break
        else:
            print("Opción no válida.")

main()

