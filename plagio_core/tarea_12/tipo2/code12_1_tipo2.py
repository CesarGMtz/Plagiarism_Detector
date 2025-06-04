import random
import string

def crear_password(tamaño=12):
    opciones = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(opciones, k=tamaño))

def generar_lote(n, tamaño=12):
    resultados = set()
    while len(resultados) < n:
        intento = crear_password(tamaño)
        resultados.add(intento)
    return list(resultados)

def ejecutar():
    try:
        total = int(input("¿Cuántas claves quieres generar?: "))
        claves = generar_lote(total)
        print("\nListado de contraseñas:")
        for idx, clave in enumerate(claves, 1):
            print(f"{idx}: {clave}")
    except:
        print("Error en la entrada.")

if __name__ == "__main__":
    ejecutar()

