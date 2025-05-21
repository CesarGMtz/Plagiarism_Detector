def ordenar(lista):
    largo = len(lista)
    for i in range(largo):
        print(f"Vuelta {i+1}:")
        for j in range(0, largo - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(" ", lista)
        print("-" * 25)
    return lista

def comenzar():
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Lista inicial:")
    print(datos)
    print("\nProceso paso a paso:")
    resultado = ordenar(datos.copy())
    print("\nResultado final:")
    print(resultado)

comenzar()

