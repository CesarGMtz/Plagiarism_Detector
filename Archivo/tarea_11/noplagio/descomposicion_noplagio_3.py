def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def descomp(n):
    primos = [i for i in range(2, n+1) if es_primo(i)]
    res = {}
    for p in primos:
        while n % p == 0:
            res[p] = res.get(p, 0) + 1
            n //= p
        if n == 1:
            break
    return res

num = int(input("Introduce número: "))
factores = descomp(num)
print(" × ".join(f"{k}^{v}" for k, v in factores.items()))

