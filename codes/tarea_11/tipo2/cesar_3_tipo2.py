def obtener_lista_factores(n):
    res = []
    candidato = 2
    while n > 1:
        if n % candidato == 0:
            res.append(candidato)
            n //= candidato
        else:
            candidato += 1
    return res

def agrupar_factores(lista):
    salida = {}
    for valor in lista:
        salida[valor] = salida.get(valor, 0) + 1
    return salida

def ejecutar():
    valor = int(input("Valor a factorizar: "))
    lista = obtener_lista_factores(valor)
    conteo = agrupar_factores(lista)
    print(" × ".join([f"{k}^{v}" for k, v in conteo.items()]))

ejecutar()

