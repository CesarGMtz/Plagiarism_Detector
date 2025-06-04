import random
import string

def generar(longitud):
    conjunto = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(conjunto, longitud))

def crear_contraseñas_unicas(cantidad, longitud):
    generadas = set()
    intentos = 0
    while len(generadas) < cantidad and intentos < cantidad * 10:
        nueva = generar(longitud)
        if nueva not in generadas:
            generadas.add(nueva)
        intentos += 1
    return list(generadas)

def main():
    n = int(input("¿Cuántas contraseñas únicas? "))
    l = int(input("Longitud de cada una: "))
    resultado = crear_contraseñas_unicas(n, l)
    print("\nResultado final:")
    for i, c in enumerate(resultado, 1):
        print(f"{i}. {c}")
    if len(resultado) < n:
        print("\nAdvertencia: No se pudieron generar todas por límite de intentos.")

if __name__ == "__main__":
    main()

