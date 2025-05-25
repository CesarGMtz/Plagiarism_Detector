def obtener_factores(n):
    primos = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            primos[divisor] = primos.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    if n > 1:
        primos[n] = 1
    return primos

def imprimir_resultado(factores):
    cadena = [f"{base}^{exp}" for base, exp in factores.items()]
    print(" × ".join(cadena))

valor = int(input("Ingresa un número entero: "))
res = obtener_factores(valor)
imprimir_resultado(res)

