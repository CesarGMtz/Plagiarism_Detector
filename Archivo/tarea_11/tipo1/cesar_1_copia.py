def calcular_factores(numero):
    resultado = {}
    i = 2
    while numero > 1:
        veces = 0
        while numero % i == 0:
            numero //= i
            veces += 1
        if veces != 0:
            resultado[i] = veces
        i += 1
    return resultado

def mostrar_factores(res):
    cadena = []
    for clave in sorted(res):
        cadena.append(f"{clave}^{res[clave]}")
    print(" × ".join(cadena))

num = int(input("Número: "))
factores = calcular_factores(num)
mostrar_factores(factores)

