def burbuja_debug(numeros):
    n = len(numeros)
    total = 0
    for i in range(n):
        cambios = 0
        print(f"Iteración {i+1}:")
        for j in range(n - i - 1):
            print(f"  Evaluando {numeros[j]} con {numeros[j+1]}")
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                cambios += 1
                total += 1
                print("   ↳ Se intercambian")
            else:
                print("   ↳ No hay cambio")
            print("   Lista:", numeros)
        if cambios == 0:
            print("Ya está ordenado.")
            break
        print()
    print("Intercambios realizados:", total)
    return numeros

def correr():
    datos = [5, 1, 4, 2, 8]
    print("Antes:", datos)
    res = burbuja_debug(datos.copy())
    print("Después:", res)

correr()

