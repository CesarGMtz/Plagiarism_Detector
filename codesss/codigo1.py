def obtener_numero_positivo(texto):
    while True:
        valor = input(texto)
        if valor.replace('.', '', 1).isdigit() and float(valor) > 0:
            return float(valor)
        print("Ingresa un número mayor que cero.")

def area_triangulo(b, h):
    return 0.5 * b * h

print("Área de un triángulo")
b = obtener_numero_positivo("Base: ")
h = obtener_numero_positivo("Altura: ")
resultado = area_triangulo(b, h)
print("El área es: {:.2f}".format(resultado))

