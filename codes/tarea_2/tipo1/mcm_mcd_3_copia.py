def euclides_mcd(x, y):
    while y:
        x, y = y, x % y
    return x

def euclides_mcm(x, y):
    return x * y // euclides_mcd(x, y)

def menu():
    print("1. MCD")
    print("2. MCM")
    print("3. Ambos")

def main():
    menu()
    try:
        opc = input("Opción: ")
        a = int(input("A: "))
        b = int(input("B: "))
        if opc == '1':
            print("MCD:", euclides_mcd(a, b))
        elif opc == '2':
            print("MCM:", euclides_mcm(a, b))
        elif opc == '3':
            print("MCD:", euclides_mcd(a, b))
            print("MCM:", euclides_mcm(a, b))
        else:
            print("Opción inválida.")
    except:
        print("Error de entrada.")

main()