import random
import string

def crear_unica(tamaño):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(caracteres, tamaño))

def generar_lote_unico(cantidad, tamaño):
    resultado = set()
    repeticiones = 0
    while len(resultado) < cantidad and repeticiones < cantidad * 10:
        intento = crear_unica(tamaño)
        if intento not in resultado:
            resultado.add(intento)
        repeticiones += 1
    return list(resultado)

def ejecutar():
    try:
        cuantos = int(input("¿Número de contraseñas únicas? "))
        largo = int(input("Longitud de cada clave: "))
        claves = generar_lote_unico(cuantos, largo)

        print("\nListado generado:")
        for idx, c in enumerate(claves, 1):
            print(f"{idx}. {c}")
        if len(claves) < cuantos:
            print("\n¡Ojo! No se alcanzó el total deseado por límite de intentos.")
    except:
        print("Entrada inválida.")

if __name__ == "__main__":
    ejecutar()

