def ver(lista, paso):
    print(f"→ Paso {paso}: {lista}")

def burbuja(lista):
    n = len(lista)
    etapa = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            ver(lista, etapa)
            etapa += 1
    return lista

def iniciar():
    nums = [29, 10, 14, 37, 13]
    print("Original:", nums)
    print("Ordenando...")
    final = burbuja(nums.copy())
    print("Resultado:", final)

iniciar()

