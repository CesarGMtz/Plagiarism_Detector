def solicitar_numeros():
    try:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        return a, b
    except ValueError:
        print("Por favor, introduce números válidos.")
        return solicitar_numeros()

def calcular_mcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calcular_mcm(x, y):
    return abs(x * y) // calcular_mcd(x, y)

def mostrar_resultado(op, a, b):
    if op == '1':
        print(f"El MCD de {a} y {b} es: {calcular_mcd(a, b)}")
    elif op == '2':
        print(f"El MCM de {a} y {b} es: {calcular_mcm(a, b)}")
    elif op == '3':
        print(f"MCD: {calcular_mcd(a, b)}")
        print(f"MCM: {calcular_mcm(a, b)}")
    else:
        print("Opción inválida.")

def iniciar():
    print("== Calculadora de MCD y MCM ==")
    print("1. Solo MCD\n2. Solo MCM\n3. Ambos")
    opcion = input("Selecciona una opción: ")
    num1, num2 = solicitar_numeros()
    mostrar_resultado(opcion, num1, num2)

if __name__ == "__main__":
    iniciar()
