def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        print(f"Iteración {i+1}:")
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(" ", lista)
        print("-" * 30)
    return lista

def main():
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:")
    print(datos)
    print("\nOrdenamiento paso a paso:")
    ordenada = bubble_sort(datos.copy())
    print("\nLista final ordenada:")
    print(ordenada)

main()

