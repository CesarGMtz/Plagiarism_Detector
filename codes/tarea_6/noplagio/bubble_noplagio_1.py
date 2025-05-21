def bubble_sort(data):
    n = len(data)
    for i in range(n):
        changed = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                changed = True
        print(f"Después del paso {i+1}: {data}")
        if not changed:
            break

def main():
    entrada = input("Ingresa números separados por espacio: ")
    lista = list(map(int, entrada.strip().split()))
    print("Ordenando con burbuja...\n")
    bubble_sort(lista)

main()

