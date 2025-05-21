def descomposicion(n):
    primos = {}
    for d in range(2, n + 1):
        while n % d == 0:
            if d in primos:
                primos[d] += 1
            else:
                primos[d] = 1
            n //= d
        if n == 1:
            break
    return primos

def presentar(primos):
    resultado = []
    for k in primos:
        resultado.append(f"{k}^{primos[k]}")
    print("Resultado:", " × ".join(resultado))

x = int(input("Número a descomponer: "))
primos = descomposicion(x)
presentar(primos)

