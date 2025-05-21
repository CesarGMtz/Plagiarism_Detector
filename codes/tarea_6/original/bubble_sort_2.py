def bubble_sort_trazado(valores):
    n = len(valores)
    total_swaps = 0
    for i in range(n):
        cambios = 0
        print(f"Ronda {i+1}:")
        for j in range(n - i - 1):
            print(f"  Comparando {valores[j]} y {valores[j+1]}")
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
                cambios += 1
                total_swaps += 1
                print("   → Intercambio realizado")
            else:
                print("   → Sin cambio")
            print("   Estado:", valores)
        if cambios == 0:
            print("Lista ya ordenada.")
            break
        print()
    print(f"Total de intercambios: {total_swaps}")
    return valores

def inicio():
    entrada = [5, 1, 4, 2, 8]
    print("Valores iniciales:", entrada)
    resultado = bubble_sort_trazado(entrada.copy())
    print("Resultado final:", resultado)

inicio()

