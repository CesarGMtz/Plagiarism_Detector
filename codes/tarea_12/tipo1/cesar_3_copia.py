import string
import random

def gen(tam):
    base = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(base, tam))

def gen_unicas(num, tam):
    resultados = set()
    intentos = 0
    limite = num * 10
    while len(resultados) < num and intentos < limite:
        clave = gen(tam)
        if clave not in resultados:
            resultados.add(clave)
        intentos += 1
    return list(resultados)

def main():
    total = int(input("Número de contraseñas únicas: "))
    size = int(input("Tamaño de cada una: "))
    claves = gen_unicas(total, size)
    print("Resultado:")
    for i, c in enumerate(claves, 1):
        print(f"{i}: {c}")
    if len(claves) < total:
        print("No se generaron todas las claves solicitadas.")

if __name__ == '__main__':
    main()

