import random

def inicializar_resultados():
    return {i: 0 for i in range(1, 7)}

def lanzar_dado():
    return random.randint(1, 6)

def simular_lanzamientos(n):
    resultados = inicializar_resultados()
    for _ in range(n):
        resultado = lanzar_dado()
        resultados[resultado] += 1
    return resultados

def mostrar(resultados):
    print("Resultados:")
    for numero, cantidad in resultados.items():
        print(f"{numero}: {cantidad}")

def ciclo():
    while True:
        try:
            n = int(input("Número de lanzamientos: "))
            if n <= 0:
                raise ValueError
            resultados = simular_lanzamientos(n)
            mostrar(resultados)
        except ValueError:
            print("Entrada no válida.")
            continue
        if input("¿Terminar? (s/n): ").lower() == "s":
            break

ciclo()

