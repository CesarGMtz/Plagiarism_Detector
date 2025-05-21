import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(caracteres, k=longitud))

def generar_varias_contraseñas(n, longitud=12):
    contraseñas = set()
    while len(contraseñas) < n:
        nueva = generar_contraseña(longitud)
        if nueva not in contraseñas:
            contraseñas.add(nueva)
    return list(contraseñas)

def main():
    cantidad = int(input("¿Cuántas contraseñas necesitas? "))
    contraseñas = generar_varias_contraseñas(cantidad)
    print("\nContraseñas generadas:")
    for i, pwd in enumerate(contraseñas, 1):
        print(f"{i}: {pwd}")

if __name__ == "__main__":
    main()

