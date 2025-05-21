def buscar_factores(n):
    primos = []
    f = 2
    while f * f <= n:
        if n % f != 0:
            f += 1
        else:
            n //= f
            primos.append(f)
    if n > 1:
        primos.append(n)
    return primos

def contar(primos):
    datos = {}
    for x in primos:
        if x in datos:
            datos[x] += 1
        else:
            datos[x] = 1
    return datos

numero = int(input("Escribe un número: "))
factores = buscar_factores(numero)
conteo = contar(factores)
print(" × ".join([f"{a}^{b}" for a, b in conteo.items()]))

