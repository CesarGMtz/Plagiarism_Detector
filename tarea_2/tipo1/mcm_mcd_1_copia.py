def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return abs(a * b) // calcular_mcd(a, b)

def pedir_numeros():
    try:
        x = int(input("Primer número: "))
        y = int(input("Segundo número: "))
        return x, y
    except ValueError:
        print("Entrada inválida.")
        return None, None

def ejecutar():
    print("Cálculo de MCD y MCM (Euclides)")
    a, b = pedir_numeros()
    if a is None or b is None:
        return
    print(f"MCD de {a} y {b} es: {calcular_mcd(a, b)}")
    print(f"MCM de {a} y {b} es: {calcular_mcm(a, b)}")

ejecutar()