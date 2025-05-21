import random
import string

def obtener_caracteres():
    return string.ascii_letters + string.digits + "!@#$%&*"

def generar_contraseña(longitud):
    caracteres = obtener_caracteres()
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def entrada_longitud():
    try:
        return int(input("¿De cuántos caracteres quieres tu contraseña?: "))
    except:
        print("Valor no válido. Usando 10 por defecto.")
        return 10

def ejecutar():
    while True:
        longitud = entrada_longitud()
        clave = generar_contraseña(longitud)
        print("Tu contraseña es:", clave)
        if input("¿Generar otra? (s/n): ").lower() == "n":
            break

ejecutar()

