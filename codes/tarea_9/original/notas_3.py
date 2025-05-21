import os

NOTAS_FILE = "notas.txt"

def cargar_notas():
    if not os.path.exists(NOTAS_FILE):
        return []
    with open(NOTAS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def guardar_notas(notas):
    with open(NOTAS_FILE, "w", encoding="utf-8") as f:
        for nota in notas:
            f.write(nota + "\n")

def agregar(notas):
    nueva = input("Escribe tu nota: ")
    notas.append(nueva)
    guardar_notas(notas)
    print("Guardada en archivo.")

def mostrar(notas):
    print("\nListado de notas:")
    for i, n in enumerate(notas, 1):
        print(f"{i}. {n}")

def borrar(notas):
    mostrar(notas)
    try:
        idx = int(input("¿Qué nota quieres eliminar?: ")) - 1
        if 0 <= idx < len(notas):
            del notas[idx]
            guardar_notas(notas)
            print("Eliminada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida.")

def ejecutar():
    notas = cargar_notas()
    while True:
        print("\n1. Agregar | 2. Ver | 3. Borrar | 4. Salir")
        op = input("Elige: ")
        if op == '1':
            agregar(notas)
        elif op == '2':
            mostrar(notas)
        elif op == '3':
            borrar(notas)
        elif op == '4':
            print("Fin.")
            break
        else:
            print("Opción incorrecta.")

ejecutar()

