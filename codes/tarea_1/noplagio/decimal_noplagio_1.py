print("Conversión de base numérica")
try:
    d = int(input("Ingresa un número decimal positivo: "))
    if d < 0:
        raise ValueError("Negativo")
except:
    print("Error: entrada inválida.")
else:
    b = ''
    if d == 0:
        b = '0'
    else:
        n = d
        while n > 0:
            b = str(n % 2) + b
            n = n // 2

    print("Decimal:", d)
    print("Binario:", b)
    print("Octal:", format(d, 'o'))
    print("Hexadecimal:", format(d, 'X'))