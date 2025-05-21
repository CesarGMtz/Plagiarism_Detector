def ordenar_burbuja_extendida(arr):
    paso = 1
    n = len(arr)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                ordenado = False
            print(f"Paso {paso}: {arr}")
            paso += 1
        n -= 1
    return arr

def programa():
    valores = [3, 1, 6, 2, 9]
    print("Original:", valores)
    final = ordenar_burbuja_extendida(valores.copy())
    print("Final:", final)

programa()

