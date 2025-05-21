import random
from collections import Counter

def lanzar_dados(n_lanzamientos):
    resultados = [random.randint(1, 6) for _ in range(n_lanzamientos)]
    return Counter(resultados)

def mostrar_histograma(contador):
    print("\nHistograma de resultados:")
    for valor in range(1, 7):
        cantidad = contador.get(valor, 0)
        print(f"{valor}: {'█' * cantidad} ({cantidad})")

def main():
    print("🎲 Simulador de Dados 🎲")
    lanzamientos = int(input("¿Cuántas veces deseas lanzar el dado? "))
    conteo = lanzar_dados(lanzamientos)
    mostrar_histograma(conteo)

main()

