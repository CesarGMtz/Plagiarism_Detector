def mostrar(lista, paso):
    print(f"Paso {paso}: {lista}")

def ordenar_burbuja(numeros):
    n = len(numeros)
    paso = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            mostrar(numeros, paso)
            paso += 1
    return numeros

def ejecutar():
    valores = [29, 10, 14, 37, 13]
    print("Lista inicial:", valores)
    print("Proceso de ordenamiento:")
    ordenados = ordenar_burbuja(valores.copy())
    print("Lista final:", ordenados)

ejecutar()

