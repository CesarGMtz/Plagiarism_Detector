import os

ARCHIVO = "notas.txt"

def leer_archivo():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo.readlines()]

def escribir_archivo(lista):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for entrada in lista:
            archivo.write(entrada + "\n")

def nueva_nota(lista):
    texto = input("Escribe una nueva nota: ")
    lista.append(texto)
    escribir_archivo(lista)
    print("Nota guardada correctamente.")

def ver_notas(lista):
    print("\nNotas guardadas:")
    for idx, contenido in enumerate(lista, 1):
        print(f"{idx}. {contenido}")

def quitar_nota(lista):
    ver_notas(lista)
    try:
        seleccion = int(input("Número de nota a eliminar: ")) - 1
        if 0 <= seleccion < len(lista):
            del lista[seleccion]
            escribir_archivo(lista)
            print("Nota eliminada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada no válida.")

def menu_notas():
    lista = leer_archivo()
    while True:
        print("\nOpciones: 1) Agregar  2) Ver  3) Eliminar  4) Salir")
        eleccion = input("Tu elección: ")
        if eleccion == '1':
            nueva_nota(lista)
        elif eleccion == '2':
            ver_notas(lista)
        elif eleccion == '3':
            quitar_nota(lista)
        elif eleccion == '4':
            print("Saliendo del gestor de notas.")
            break
        else:
            print("Opción no reconocida.")

menu_notas()

