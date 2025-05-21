def mostrar_paso(lista, paso):
    print(f"Paso {paso}: {lista}")

def burbuja_mejorada(valores):
    n = len(valores)
    paso = 1
    for i in range(n):
        intercambiado = False
        for j in range(n - i - 1):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
                intercambiado = True
            mostrar_paso(valores, paso)
            paso += 1
        if not intercambiado:
            break
    return valores

def main():
    lista = [7, 4, 5, 3, 8]
    print("Lista antes:", lista)
    ordenada = burbuja_mejorada(lista.copy())
    print("Lista después:", ordenada)

main()

