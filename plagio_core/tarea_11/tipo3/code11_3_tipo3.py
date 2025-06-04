def factorizar(n):
    i = 2
    factores = []
    while i * i <= n:
        if n % i == 0:
            factores.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factores.append(n)
    return factores

def conteo(factores):
    resultado = {}
    for f in factores:
        resultado[f] = resultado.get(f, 0) + 1
    return resultado

def imprimir(resultado):
    for base, potencia in resultado.items():
        print(f"{base}^{potencia}")

def ejecutar():
    while True:
        try:
            entrada = int(input("Número entero: "))
            if entrada <= 1:
                raise ValueError
        except ValueError:
            print("Número inválido. Intenta de nuevo.")
            continue
        factores = factorizar(entrada)
        imprimir(conteo(factores))
        if input("¿Finalizar? (s/n): ").lower() == 's':
            break

ejecutar()

