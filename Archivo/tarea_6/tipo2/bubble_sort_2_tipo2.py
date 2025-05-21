def ordenar(lista):
    n = len(lista)
    paso = 1
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            paso += 1
    return lista

def seguimiento(lista_original):
    lista = lista_original.copy()
    n = len(lista)
    paso = 1
    print("Trazado de pasos:")
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            print(f"Paso {paso}: {lista}")
            paso += 1

def ejecutar():
    datos = [30, 20, 10, 50, 40]
    seguimiento(datos)

ejecutar()

