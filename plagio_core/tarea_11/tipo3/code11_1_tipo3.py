def calcular_factores(n):
    factores = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores[divisor] = factores.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    return factores

def imprimir_factores(diccionario):
    for base, exponente in diccionario.items():
        print(f"{base}^{exponente}")

def leer_numero():
    try:
        return int(input("Introduce un número entero: "))
    except ValueError:
        print("Entrada inválida.")
        return None

def proceso():
    while True:
        numero = leer_numero()
        if numero is None or numero <= 1:
            print("Debe ser mayor que 1.")
            continue
        resultado = calcular_factores(numero)
        imprimir_factores(resultado)
        if input("¿Terminar? (s/n): ").lower() == 's':
            break

proceso()

