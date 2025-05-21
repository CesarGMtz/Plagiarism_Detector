def obtener_mcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def obtener_mcm(x, y):
    return (x * y) // obtener_mcd(x, y)

def solicitar_datos():
    try:
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        return a, b
    except ValueError:
        print("Error: Entrada no válida.")
        return None, None

def mostrar_resultados(a, b):
    print(f"MCD({a}, {b}) = {obtener_mcd(a, b)}")
    print(f"MCM({a}, {b}) = {obtener_mcm(a, b)}")

def principal():
    while True:
        a, b = solicitar_datos()
        if a is None:
            continue
        mostrar_resultados(a, b)
        salir = input("¿Deseas salir? (s/n): ")
        if salir.lower() == 's':
            break

principal()

