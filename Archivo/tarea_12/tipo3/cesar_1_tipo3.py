import random
import string

def construir_conjunto(segura=True):
    if segura:
        return string.ascii_letters + string.digits + string.punctuation
    return string.ascii_lowercase

def crear_contraseña(longitud, segura=True):
    conjunto = construir_conjunto(segura)
    return ''.join(random.choice(conjunto) for _ in range(longitud))

def solicitar_datos():
    try:
        longitud = int(input("Longitud de la contraseña: "))
        modo = input("¿Segura? (s/n): ").lower() == 's'
        return longitud, modo
    except:
        print("Datos inválidos.")
        return 8, True

def flujo():
    while True:
        longitud, segura = solicitar_datos()
        print("Contraseña generada:", crear_contraseña(longitud, segura))
        if input("¿Finalizar? (s/n): ").lower() == 's':
            break

flujo()

