def contar_factores(n, d=2, conteo=None):
    if conteo is None:
        conteo = {}
    if d > n:
        return conteo
    if n % d == 0:
        conteo[d] = conteo.get(d, 0) + 1
        return contar_factores(n // d, d, conteo)
    return contar_factores(n, d + 1, conteo)

numero = int(input("Número a descomponer: "))
factores = contar_factores(numero)
print(" × ".join(f"{k}^{v}" for k, v in factores.items()))

