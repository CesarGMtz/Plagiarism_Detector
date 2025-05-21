import random
import string

def crear_pool():
    return string.ascii_letters + string.digits + string.punctuation

def generar(longitud):
    pool = crear_pool()
    return ''.join(random.choice(pool) for _ in range(longitud))

def solicitar_longitud():
    try:
        return int(input("Longitud de contraseña: "))
    except ValueError:
        print("Entrada inválida, usando 12.")
        return 12

def iniciar():
    while True:
        cantidad = solicitar_longitud()
        clave = generar(cantidad)
        print("Clave generada:", clave)
        if input("¿Salir? (s/n): ").lower() == "s":
            break

iniciar()

