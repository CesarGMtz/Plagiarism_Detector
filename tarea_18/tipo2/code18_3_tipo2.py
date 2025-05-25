def extraer_fragmentos(linea, objetivo, alcance=2):
    tokens = linea.split()
    resultados = []
    for idx, palabra in enumerate(tokens):
        if palabra.lower() == objetivo.lower():
            inicio = max(0, idx - alcance)
            fin = min(len(tokens), idx + alcance + 1)
            resultados.append(' '.join(tokens[inicio:fin]))
    return resultados

def explorar_archivo(ruta, clave):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()

    total = 0
    for i, fila in enumerate(contenido, 1):
        secciones = extraer_fragmentos(fila, clave)
        for fragmento in secciones:
            total += 1
            print(f"Línea {i}: {fragmento}")

    print(f"\nTotal de apariciones de '{clave}': {total}")

ruta_archivo = 'documento.txt'
termino = input("Palabra clave a buscar: ")
explorar_archivo(ruta_archivo, termino)

