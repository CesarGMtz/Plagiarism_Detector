def burbuja_interactiva(lista):
    longitud = len(lista)
    for i in range(longitud):
        print(f"Iteración {i + 1}")
        for j in range(0, longitud - i - 1):
            print(f"Comparando {lista[j]} y {lista[j + 1]}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f" => Intercambiado: {lista}")
    return lista

def obtener_entrada():
    try:
        entrada = input("Ingresa números separados por comas: ")
        return [int(x.strip()) for x in entrada.split(",")]
    except:
        print("Entrada inválida.")
        return []

def iniciar():
    while True:
        datos = obtener_entrada()
        if datos:
            resultado = burbuja_interactiva(datos)
            print("Lista ordenada:", resultado)
            if input("¿Deseas salir? (s/n): ").lower() == "s":
                break

iniciar()

