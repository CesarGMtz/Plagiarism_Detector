import random
import string

def generar_letras():
    return string.ascii_letters + string.digits + string.punctuation

def nueva_clave(n):
    caracteres = generar_letras()
    return ''.join(random.choice(caracteres) for _ in range(n))

def generar_todas(m, longitud):
    claves = []
    while True:
        clave = nueva_clave(longitud)
        if clave not in claves:
            claves.append(clave)
        if len(claves) == m:
            break
    return claves

def mostrar_resultado(lista):
    print("\nClaves creadas:")
    for c in lista:
        print("-", c)

def main():
    cantidad = int(input("¿Cuántas claves quieres? "))
    longitud = 12
    resultado = generar_todas(cantidad, longitud)
    mostrar_resultado(resultado)

main()

