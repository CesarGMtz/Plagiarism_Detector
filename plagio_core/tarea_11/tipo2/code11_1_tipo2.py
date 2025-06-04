def factores_primos(valor):
    resultado = {}
    actual = 2
    while valor > 1:
        repeticiones = 0
        while valor % actual == 0:
            valor //= actual
            repeticiones += 1
        if repeticiones > 0:
            resultado[actual] = repeticiones
        actual += 1
    return resultado

def mostrar(resultado):
    partes = [f"{n}^{p}" for n, p in sorted(resultado.items())]
    print(" × ".join(partes))

if __name__ == "__main__":
    entrada = int(input("Número a descomponer: "))
    primos = factores_primos(entrada)
    mostrar(primos)

