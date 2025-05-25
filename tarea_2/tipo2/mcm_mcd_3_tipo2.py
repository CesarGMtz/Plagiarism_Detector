def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return a * b // calcular_mcd(a, b)

def mostrar_menu():
    print("Elige una opción:")
    print("1 - Solo MCD")
    print("2 - Solo MCM")
    print("3 - MCD y MCM")

def ejecutar():
    mostrar_menu()
    try:
        opcion = input("Tu opción: ")
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))

        if opcion == '1':
            print("Resultado MCD =", calcular_mcd(n1, n2))
        elif opcion == '2':
            print("Resultado MCM =", calcular_mcm(n1, n2))
        elif opcion == '3':
            print("MCD:", calcular_mcd(n1, n2))
            print("MCM:", calcular_mcm(n1, n2))
        else:
            print("Opción no válida.")
    except:
        print("Entrada inválida.")

ejecutar()

