def calcular_mcd_recursivo(x, y):
    return x if y == 0 else calcular_mcd_recursivo(y, x % y)

def calcular_mcm(x, y):
    return abs(x * y) // calcular_mcd_recursivo(x, y)

def leer_valores():
    try:
        x = int(input("Número A: "))
        y = int(input("Número B: "))
        return x, y
    except:
        print("Entrada inválida.")
        return None, None

def resultado_mcd_mcm(x, y):
    print(f"→ MCD: {calcular_mcd_recursivo(x, y)}")
    print(f"→ MCM: {calcular_mcm(x, y)}")

def inicio():
    while True:
        x, y = leer_valores()
        if x is None:
            continue
        resultado_mcd_mcm(x, y)
        if input("¿Salir? (s/n): ").lower() == 's':
            break

inicio()

