import random
import string

def construir_contraseña(tamaño):
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(random.choice(pool) for _ in range(tamaño))

def generar_conjunto(cantidad, tamaño):
    conjunto = set()
    while len(conjunto) < cantidad:
        conjunto.add(construir_contraseña(tamaño))
    return sorted(conjunto)

def main():
    cantidad = int(input("Número de claves deseadas: "))
    longitud = 12
    claves = generar_conjunto(cantidad, longitud)
    print("\nClaves seguras:")
    [print(f"Clave #{i+1}: {clave}") for i, clave in enumerate(claves)]

main()

