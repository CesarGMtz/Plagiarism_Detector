def analizar_bloques(ruta, objetivo, bloque_tam=5):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    ocurrencias = 0
    bloques = []

    for i in range(0, len(lineas), bloque_tam):
        bloque = lineas[i:i + bloque_tam]
        bloque_str = ''.join(bloque).lower()
        if objetivo.lower() in bloque_str:
            ocurrencias += bloque_str.count(objetivo.lower())
            bloques.append(bloque)

    print(f"La palabra '{objetivo}' aparece {ocurrencias} veces.")
    for j, b in enumerate(bloques, 1):
        print(f"\n--- Bloque {j} ---\n{''.join(b)}")

archivo = 'documento.txt'
palabra = input("Palabra a buscar: ")
analizar_bloques(archivo, palabra)

