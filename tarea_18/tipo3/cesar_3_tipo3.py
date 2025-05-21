def encontrar_con_contexto(path, keyword, rango=2):
    from itertools import islice
    with open(path, 'r', encoding='utf-8') as file:
        datos = file.readlines()

    total = 0
    for idx in range(len(datos)):
        palabras = datos[idx].split()
        for i in range(len(palabras)):
            if palabras[i].lower() == keyword.lower():
                inicio = max(i - rango, 0)
                fin = min(i + rango + 1, len(palabras))
                contexto = " ".join(palabras[inicio:fin])
                print(f"Línea {idx + 1} -> {contexto}")
                total += 1

    print(f"\nSe halló la palabra '{keyword}' en {total} ocasiones.")

archivo_txt = 'documento.txt'
palabra_objetivo = input("Palabra a localizar: ")
encontrar_con_contexto(archivo_txt, palabra_objetivo)

