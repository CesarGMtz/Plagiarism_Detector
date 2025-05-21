def factores_primos(num):
    resultado = {}
    i = 2
    while i * i <= num:
        while num % i == 0:
            resultado[i] = resultado.get(i, 0) + 1
            num //= i
        i += 1
    if num > 1:
        resultado[num] = 1
    return resultado

def mostrar(resultados):
    factores = [f"{p}^{e}" for p, e in resultados.items()]
    print(" × ".join(factores))

n = int(input("Número a descomponer: "))
res = factores_primos(n)
mostrar(res)

