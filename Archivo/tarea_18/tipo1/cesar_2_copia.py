def contar_y_buscar_palabra(ruta, palabra_buscada):
    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    total = 0
    resultados = []

    for i, linea in enumerate(lineas):
        if palabra_buscada.lower() in linea.lower():
            total += 1
            resultados.append((i + 1, linea.strip()))

    print(f"La palabra '{palabra_buscada}' se encontró {total} veces.")
    for num, texto in resultados:
        print(f"Línea {num}: {texto}")

archivo_objetivo = 'documento.txt'
palabra = input("Buscar: ")
contar_y_buscar_palabra(archivo_objetivo, palabra)

