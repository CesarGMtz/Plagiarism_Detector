def es_numero_positivo(valor):
    try:
        numero = float(valor)
        return numero > 0
    except ValueError:
        return False

def pedir_valor(mensaje):
    while True:
        entrada = input(mensaje)
        if es_numero_positivo(entrada):
            return float(entrada)
        print("Por favor ingresa un número válido y positivo.")

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    print("Cálculo del área de un triángulo")
    base = pedir_valor("Introduce la base: ")
    altura = pedir_valor("Introduce la altura: ")
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")

if __name__ == "__main__":
    main()

