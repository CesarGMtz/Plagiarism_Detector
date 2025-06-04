def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_circulo(radio):
    pi = 3.1416
    return pi * radio * radio

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def menu():
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo")

def ejecutar():
    menu()
    opcion = int(input("Elige una figura: "))
    if opcion == 1:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", calcular_area_rectangulo(b, h))
    elif opcion == 2:
        r = float(input("Radio: "))
        print("Área:", calcular_area_circulo(r))
    elif opcion == 3:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", calcular_area_triangulo(b, h))
    else:
        print("Opción inválida")

if __name__ == "__main__":
    ejecutar()

