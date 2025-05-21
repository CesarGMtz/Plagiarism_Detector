def descomponer(num):
    i = 2
    factores = {}
    while i * i <= num:
        while num % i == 0:
            factores[i] = factores.get(i, 0) + 1
            num //= i
        i += 1
    if num > 1:
        factores[num] = 1
    return factores

def mostrar_resultado(factores):
    print("Factores primos:")
    for p, count in factores.items():
        print(f"{p}^{count}")

def solicitar_entrada():
    entrada = input("Número para descomponer: ")
    try:
        return int(entrada)
    except:
        return -1

def main():
    while True:
        n = solicitar_entrada()
        if n <= 1:
            print("Número inválido.")
            continue
        factores = descomponer(n)
        mostrar_resultado(factores)
        if input("¿Salir? (s/n): ").lower() == "s":
            break

main()

