import os

ARCHIVO = "archivo_notas.txt"

def leer():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def guardar(notas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for nota in notas:
            f.write(nota + "\n")

def nueva(notas):
    n = input("Nota nueva: ")
    notas.append(n)
    guardar(notas)
    print("Nota escrita.")

def listar(notas):
    print("\nNotas:")
    for i, n in enumerate(notas, 1):
        print(f"{i}. {n}")

def eliminar(notas):
    listar(notas)
    try:
        x = int(input("¿Cuál borrar?: ")) - 1
        if 0 <= x < len(notas):
            notas.pop(x)
            guardar(notas)
            print("Eliminada.")
        else:
            print("Índice fuera.")
    except:
        print("Inválido.")

def main():
    notas = leer()
    while True:
        print("\n1.Agregar 2.Ver 3.Borrar 4.Salir")
        op = input("Opción: ")
        if op == '1':
            nueva(notas)
        elif op == '2':
            listar(notas)
        elif op == '3':
            eliminar(notas)
        elif op == '4':
            break

main()

