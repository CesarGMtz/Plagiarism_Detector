def contar_ocurrencias(archivo, termino):
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    total = 0
    resultados = []

    for num, texto in enumerate(lineas, 1):
        if termino.lower() in texto.lower():
            total += 1
            resultados.append((num, texto.strip()))

    print(f"\nSe encontró '{termino}' {total} veces.\n")
    for fila, contenido in resultados:
        print(f"Línea {fila}: {contenido}")

ruta = 'documento.txt'
buscado = input("¿Qué palabra deseas buscar?: ")
contar_ocurrencias(ruta, buscado)

