import random

def contar_dados(veces):
    datos = [0] * 6
    for _ in range(veces):
        cara = random.randint(1, 6)
        datos[cara - 1] += 1
    return datos

def mostrar(datos):
    print("\nResumen:")
    total = sum(datos)
    for i, cant in enumerate(datos, 1):
        porc = (cant / total) * 100
        print(f"{i} → {cant} veces ({porc:.2f}%)")

def ejecutar():
    intentos = int(input("Ingresa el número de lanzamientos: "))
    datos = contar_dados(intentos)
    mostrar(datos)

ejecutar()

