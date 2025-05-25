def obtener_mcd(x, y):
    if y == 0:
        return x
    return obtener_mcd(y, x % y)

def obtener_mcm(x, y):
    return abs(x * y) // obtener_mcd(x, y)

def pedir_entero(texto):
    while True:
        try:
            return int(input(texto))
        except:
            print("Entrada no válida.")

def ejecutar():
    print("=== Cálculo de MCD y MCM ===")
    a = pedir_entero("Ingresa primer número: ")
    b = pedir_entero("Ingresa segundo número: ")

    print("Resultado MCD:", obtener_mcd(a, b))
    print("Resultado MCM:", obtener_mcm(a, b))

ejecutar()

