import random

def lanzar_veces(cantidad):
    conteo = {x: 0 for x in range(1, 7)}
    for _ in range(cantidad):
        cara = random.randint(1, 6)
        conteo[cara] += 1
    return conteo

def mostrar_barras(conteo):
    print("\nFrecuencias obtenidas:")
    for num in range(1, 7):
        barras = conteo[num] // 10
        print(f"{num} → {'#' * barras} ({conteo[num]})")

def correr():
    try:
        veces = int(input("¿Cuántas veces lanzar el dado? "))
        resultado = lanzar_veces(veces)
        mostrar_barras(resultado)
    except:
        print("Error en la entrada.")

correr()

