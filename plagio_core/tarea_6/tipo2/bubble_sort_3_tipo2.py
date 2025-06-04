def imprimir_paso(elementos, contador):
    print(f"Paso {contador}: {elementos}")

def metodo_burbuja(valores):
    total = len(valores)
    contador = 1
    for i in range(total - 1):
        for j in range(total - i - 1):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
            imprimir_paso(valores, contador)
            contador += 1
    return valores

def iniciar():
    datos = [29, 10, 14, 37, 13]
    print("Lista original:", datos)
    print("Ordenando...")
    final = metodo_burbuja(datos.copy())
    print("Resultado final:", final)

iniciar()

