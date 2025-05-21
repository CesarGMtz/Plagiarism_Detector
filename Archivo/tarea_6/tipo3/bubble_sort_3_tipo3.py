def imprimir_progreso(lista, iteracion):
    print(f"Estado en paso {iteracion}: {lista}")

def bubble_sort_completo(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        imprimir_progreso(lista, i + 1)
    return lista

def leer_lista():
    entrada = input("Introduce lista de enteros (separados por coma): ")
    try:
        return [int(x) for x in entrada.split(",")]
    except ValueError:
        print("Error al leer la lista.")
        return []

def ejecutar():
    while True:
        datos = leer_lista()
        if datos:
            bubble_sort_completo(datos)
        if input("¿Repetir? (s/n): ").lower() == "n":
            break

ejecutar()

