def mcd_euclides(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm_euclides(a, b):
    return abs(a * b) // mcd_euclides(a, b)

def entrada_valores():
    try:
        x = int(input("Introduce el primer número: "))
        y = int(input("Introduce el segundo número: "))
        return x, y
    except ValueError:
        print("Entrada inválida.")
        return None, None

def operaciones(a, b):
    print("== RESULTADOS ==")
    print("MCD =", mcd_euclides(a, b))
    print("MCM =", mcm_euclides(a, b))

def ejecutar_aplicacion():
    while True:
        x, y = entrada_valores()
        if x is None:
            continue
        operaciones(x, y)
        salir = input("¿Terminar? (s/n): ")
        if salir.strip().lower() == 's':
            break

ejecutar_aplicacion()

