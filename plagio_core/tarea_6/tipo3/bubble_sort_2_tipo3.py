def ordenar_y_contar(lista):
    n = len(lista)
    intercambios = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return lista, intercambios

def pedir_datos():
    try:
        numeros = input("Números separados por espacio: ")
        return [int(x) for x in numeros.split()]
    except:
        return []

def principal():
    while True:
        datos = pedir_datos()
        if not datos:
            print("Intenta de nuevo.")
            continue
        ordenada, swaps = ordenar_y_contar(datos)
        print("Resultado:", ordenada)
        print("Intercambios realizados:", swaps)
        if input("¿Salir? (s/n): ").strip().lower() == "s":
            break

principal()

