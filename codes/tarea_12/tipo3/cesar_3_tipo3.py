import string
import random

def caracteres_seguridad():
    return ''.join([
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ])

def clave_completa(longitud):
    base = string.ascii_letters + string.digits + string.punctuation
    restante = ''.join(random.choice(base) for _ in range(longitud - 3))
    return ''.join(random.sample(caracteres_seguridad() + restante, longitud))

def crear_conjunto(n, l):
    claves = []
    while len(claves) < n:
        nueva = clave_completa(l)
        if nueva not in claves:
            claves.append(nueva)
    return claves

def mostrar(claves):
    for idx, clave in enumerate(claves, 1):
        print(f"{idx}. {clave}")

def main():
    c = int(input("Cantidad de contraseñas: "))
    tam = int(input("Tamaño de contraseña: "))
    claves_generadas = crear_conjunto(c, tam)
    mostrar(claves_generadas)

main()

