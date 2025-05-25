from collections import defaultdict

def generador_factores(n):
    d = 2
    while n > 1:
        if n % d == 0:
            yield d
            n //= d
        else:
            d += 1

n = int(input("Ingresa número: "))
frecuencia = defaultdict(int)

for f in generador_factores(n):
    frecuencia[f] += 1

print(" × ".join(f"{k}^{v}" for k, v in sorted(frecuencia.items())))

