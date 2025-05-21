def descomponer_factores(n):
    factores = {}
    divisor = 2
    while n > 1:
        contador = 0
        while n % divisor == 0:
            n //= divisor
            contador += 1
        if contador > 0:
            factores[divisor] = contador
        divisor += 1
    return factores

def imprimir_factores(factores):
    salida = []
    for factor in sorted(factores):
        salida.append(f"{factor}^{factores[factor]}")
    print(" × ".join(salida))

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    factores = descomponer_factores(numero)
    imprimir_factores(factores)

