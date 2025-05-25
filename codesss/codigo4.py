def area_rect(b, h):
    return b * h

def area_circ(r):
    return 3.1416 * r**2

def area_tri(b, h):
    return 0.5 * b * h

def mostrar_menu():
    opciones = ["Rectángulo", "Círculo", "Triángulo"]
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")

def main():
    mostrar_menu()
    eleccion = int(input("Selecciona una opción: "))
    if eleccion == 1:
        base = float(input("Base: "))
        alto = float(input("Altura: "))
        print("Área:", area_rect(base, alto))
    elif eleccion == 2:
        r = float(input("Radio: "))
        print("Área:", area_circ(r))
    elif eleccion == 3:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", area_tri(b, h))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


