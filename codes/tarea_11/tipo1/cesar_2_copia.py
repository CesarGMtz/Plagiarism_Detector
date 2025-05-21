def primos_descomp(n):
    datos = {}
    div = 2
    while div * div <= n:
        while n % div == 0:
            datos[div] = datos.get(div, 0) + 1
            n //= div
        div += 1
    if n > 1:
        datos[n] = 1
    return datos

def salida(fact):
    lista = []
    for base, exp in fact.items():
        lista.append(f"{base}^{exp}")
    print(" × ".join(lista))

valor = int(input("Ingrese un número: "))
resultado = primos_descomp(valor)
salida(resultado)

