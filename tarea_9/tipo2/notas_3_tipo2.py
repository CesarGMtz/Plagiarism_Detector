import os

ARCHIVO = "registro_notas.txt"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    return []

def guardar(notas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for n in notas:
            f.write(n + "\n")

def añadir(notas):
    nueva = input("Nota: ")
    notas.append(nueva)
    guardar(notas)

def mostrar(notas):
    for i, n in enumerate(notas, 1):
        print(f"{i}) {n}")

def borrar(notas):
    mostrar(notas)
    try:
        idx = int(input("Eliminar número: ")) - 1
        if 0 <= idx < len(notas):
            del notas[idx]
            guardar(notas)
    except:
        print("Error.")

def main():
    notas = cargar()
    acciones = {
        '1': añadir,
        '2': mostrar,
        '3': borrar,
    }
    while True:
        print("\n1. Agregar 2. Ver 3. Borrar 4. Salir")
        op = input("Selecciona: ")
        if op == '4':
            break
        elif op in acciones:
            acciones[op](notas)
        else:
            print("Inválido.")

main()

