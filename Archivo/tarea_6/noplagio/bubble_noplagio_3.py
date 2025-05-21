def paso_visual(lista, paso):
    print(f"🔁 Paso {paso:02d}: {lista}")

def ordenamiento_burbuja(arr):
    n = len(arr)
    step = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            paso_visual(arr, step)
            step += 1
    return arr

def interactivo():
    print("✳ Ordenamiento por burbuja con pasos visuales ✳")
    datos = [15, 7, 3, 12, 9]
    ordenamiento_burbuja(datos)

interactivo()

