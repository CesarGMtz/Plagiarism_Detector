def descomponer_primos(valor):
    divisor = 2
    lista = []
    while divisor * divisor <= valor:
        if valor % divisor:
            divisor += 1
        else:
            valor //= divisor
            lista.append(divisor)
    if valor > 1:
        lista.append(valor)
    return lista

def agrupar_factores(lista):
    resultado = {}
    for elem in lista:
        resultado[elem] = resultado.get(elem, 0) + 1
    return resultado

def ejecutar():
    numero = int(input("Número a analizar: "))
    factores = descomponer_primos(numero)
    conteo = agrupar_factores(factores)
    print(" × ".join(f"{clave}^{valor}" for clave, valor in conteo.items()))

ejecutar()

