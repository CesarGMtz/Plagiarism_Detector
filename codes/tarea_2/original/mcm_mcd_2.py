def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

def leer_numero(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Número inválido.")

def iniciar():
    print("Calculadora MCD/MCM")
    n1 = leer_numero("Número 1: ")
    n2 = leer_numero("Número 2: ")

    print("MCD:", mcd(n1, n2))
    print("MCM:", mcm(n1, n2))

iniciar()