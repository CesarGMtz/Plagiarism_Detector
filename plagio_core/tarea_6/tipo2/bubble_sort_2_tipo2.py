def burbuja_con_detalle(datos):
    n = len(datos)
    intercambios = 0

    for i in range(n):
        cambios_ronda = 0
        print(f"Iteración {i+1}:")
        for j in range(n - i - 1):
            print(f"  Comparando {datos[j]} vs {datos[j+1]}")
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                cambios_ronda += 1
                intercambios += 1
                print("   → Se intercambió")
            else:
                print("   → Sin cambio")
            print("   Actual:", datos)
        if cambios_ronda == 0:
            print("La lista ya está ordenada.")
            break
        print()
    print(f"Total de intercambios hechos: {intercambios}")
    return datos

def ejecutar():
    muestra = [5, 1, 4, 2, 8]
    print("Lista original:", muestra)
    resultado = burbuja_con_detalle(muestra.copy())
    print("Lista ordenada:", resultado)

ejecutar()

