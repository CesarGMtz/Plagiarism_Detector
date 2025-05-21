def obtener_factores_primos(n):
    i = 2
    factores = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factores.append(i)
    if n > 1:
        factores.append(n)
    return factores

def contar_factores(factores):
    conteo = {}
    for f in factores:
        conteo[f] = conteo.get(f, 0) + 1
    return conteo

def main():
    num = int(input("Introduce un número entero: "))
    primos = obtener_factores_primos(num)
    conteo = contar_factores(primos)
    salida = " × ".join([f"{k}^{v}" for k, v in conteo.items()])
    print(salida)

main()

