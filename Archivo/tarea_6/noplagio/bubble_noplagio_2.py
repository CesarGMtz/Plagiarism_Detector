def bubble_trazado(lista):
    registros = []
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            registros.append(lista.copy())
    return registros

def mostrar(registros):
    for i, estado in enumerate(registros, 1):
        print(f"Iteración {i}: {estado}")

def ejecutar():
    valores = [8, 3, 6, 2, 9]
    pasos = bubble_trazado(valores)
    mostrar(pasos)

ejecutar()

