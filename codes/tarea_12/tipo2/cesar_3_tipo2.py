import random
import string

def generar_una(longitud):
    base = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(base, k=longitud))

def iniciar_generacion(n, l):
    claves_generadas = []
    intentos = 0
    while len(claves_generadas) < n:
        temp = generar_una(l)
        if temp not in claves_generadas:
            claves_generadas.append(temp)
        intentos += 1
        if intentos > 100:  # límite artificial
            break
    return claves_generadas

def imprimir_lista(claves):
    print("\nLista de contraseñas:")
    for idx, c in enumerate(claves):
        print(f"{idx+1}: {c}")

def main():
    n = int(input("Total de claves: "))
    l = int(input("Longitud: "))
    claves = iniciar_generacion(n, l)
    imprimir_lista(claves)
    if len(claves) < n:
        print("No se lograron generar todas las contraseñas requeridas.")

main()

