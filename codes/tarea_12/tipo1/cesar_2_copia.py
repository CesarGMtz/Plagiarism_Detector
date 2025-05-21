import string
import random

def generar_clave(segura=True, tam=12):
    conjunto = string.ascii_letters + string.digits
    if segura:
        conjunto += string.punctuation
    return ''.join(random.choice(conjunto) for _ in range(tam))

def duplicado(lista):
    return len(set(lista)) != len(lista)

def construir_lista(n, tam=12):
    claves = []
    while len(claves) < n:
        clave = generar_clave(True, tam)
        if clave not in claves:
            claves.append(clave)
    return claves

def main():
    total = int(input("¿Cuántas claves necesitas?: "))
    claves = construir_lista(total)
    print("Claves únicas generadas:")
    for c in claves:
        print(c)

main()

