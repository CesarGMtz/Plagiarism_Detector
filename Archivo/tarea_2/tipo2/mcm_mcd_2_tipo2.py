def encontrar_mcd(x, y):
    return x if y == 0 else encontrar_mcd(y, x % y)

def encontrar_mcm(x, y):
    return abs(x * y) // encontrar_mcd(x, y)

def solicitar_valor(texto):
    while True:
        entrada = input(texto)
        if entrada.isdigit():
            return int(entrada)
        print("Entrada no válida.")

def principal():
    print("Herramienta para MCD y MCM")
    val1 = solicitar_valor("Introduce número A: ")
    val2 = solicitar_valor("Introduce número B: ")

    print("MCD:", encontrar_mcd(val1, val2))
    print("MCM:", encontrar_mcm(val1, val2))

principal()