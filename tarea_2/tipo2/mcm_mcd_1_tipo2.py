def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

def leer_datos():
    try:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        return n1, n2
    except ValueError:
        print("Error: entrada inválida.")
        return None, None

def main():
    print("== MCD y MCM con algoritmo de Euclides ==")
    n1, n2 = leer_datos()
    if n1 is None or n2 is None:
        return
    print(f"El MCD de {n1} y {n2} es {mcd(n1, n2)}")
    print(f"El MCM de {n1} y {n2} es {mcm(n1, n2)}")

main()

