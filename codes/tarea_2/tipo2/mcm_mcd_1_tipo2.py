def maximo_comun_divisor(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def minimo_comun_multiplo(n1, n2):
    return abs(n1 * n2) // maximo_comun_divisor(n1, n2)

def leer_entrada():
    try:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        return a, b
    except:
        print("Entrada inválida")
        return None, None

def iniciar():
    print("Programa para calcular MCD y MCM")
    num1, num2 = leer_entrada()
    if num1 is not None and num2 is not None:
        print("MCD:", maximo_comun_divisor(num1, num2))
        print("MCM:", minimo_comun_multiplo(num1, num2))

iniciar()