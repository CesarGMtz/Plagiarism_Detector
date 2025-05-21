def imprimir_resultado(diccionario):
    partes = [f"{clave}^{valor}" for clave, valor in diccionario.items()]
    print(" × ".join(partes))

def obtener_primos(numero):
    divisores = {}
    actual = 2
    while numero > 1:
        if numero % actual == 0:
            divisores[actual] = divisores.get(actual, 0) + 1
            numero //= actual
        else:
            actual += 1
    return divisores

if __name__ == "__main__":
    n = int(input("Escribe un número entero: "))
    resultado = obtener_primos(n)
    imprimir_resultado(resultado)

