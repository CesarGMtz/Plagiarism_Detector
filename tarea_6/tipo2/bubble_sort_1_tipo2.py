def ordenar_burbuja(arreglo):
    total = len(arreglo)
    for i in range(total):
        print(f"Vuelta {i+1}:")
        for j in range(0, total - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
            print(" ", arreglo)
        print("-" * 30)
    return arreglo

def ejecutar():
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista inicial:")
    print(numeros)
    print("\nOrdenando paso a paso:")
    resultado = ordenar_burbuja(numeros.copy())
    print("\nLista ordenada:")
    print(resultado)

ejecutar()

