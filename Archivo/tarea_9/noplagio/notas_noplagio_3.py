import os

ARCH = "data_notes.txt"

def load_notes():
    if not os.path.exists(ARCH):
        return []
    return open(ARCH).read().splitlines()

def save_notes(notas):
    with open(ARCH, "w") as f:
        f.write("\n".join(notas))

def add(notas):
    nota = input("Nueva nota: ")
    notas.append(nota)
    save_notes(notas)

def view(notas):
    print("\n".join([f"{i+1}. {n}" for i, n in enumerate(notas)]))

def remove(notas):
    view(notas)
    try:
        idx = int(input("Eliminar número: ")) - 1
        if 0 <= idx < len(notas):
            del notas[idx]
            save_notes(notas)
    except:
        print("Error al eliminar.")

def main():
    notas = load_notes()
    while True:
        print("\n1.Agregar 2.Ver 3.Eliminar 4.Salir")
        o = input("Elige: ")
        if o == '1':
            add(notas)
        elif o == '2':
            view(notas)
        elif o == '3':
            remove(notas)
        elif o == '4':
            break

main()

