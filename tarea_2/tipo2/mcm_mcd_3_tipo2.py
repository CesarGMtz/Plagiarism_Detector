def mcd_euclides(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm_euclides(a, b):
    return a * b // mcd_euclides(a, b)

def opciones():
    return {
        '1': lambda x, y: print("MCD:", mcd_euclides(x, y)),
        '2': lambda x, y: print("MCM:", mcm_euclides(x, y)),
        '3': lambda x, y: (print("MCD:", mcd_euclides(x, y)), print("MCM:", mcm_euclides(x, y)))
    }

def main():
    print("Selecciona:")
    print("1. Solo MCD")
    print("2. Solo MCM")
    print("3. Ambos")
    try:
        opt = input("Opción: ")
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        accion = opciones().get(opt)
        if accion:
            accion(n1, n2)
        else:
            print("Opción inválida.")
    except:
        print("Error en los datos ingresados.")

main()