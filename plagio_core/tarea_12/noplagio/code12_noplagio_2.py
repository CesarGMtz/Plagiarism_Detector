import random
import string

def generador_contraseñas(longitud=12):
    base = string.ascii_letters + string.digits + string.punctuation
    generadas = set()
    while True:
        pwd = ''.join(random.choices(base, k=longitud))
        if pwd not in generadas:
            generadas.add(pwd)
            yield pwd

def main():
    cantidad = int(input("¿Cuántas contraseñas únicas? "))
    gen = generador_contraseñas()
    print("\nGenerando contraseñas:")
    for i in range(cantidad):
        print(f"{i+1} -> {next(gen)}")

main()

