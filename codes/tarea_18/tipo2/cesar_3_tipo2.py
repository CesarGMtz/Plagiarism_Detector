def extraer_fragmentos(texto, clave, alcance=2):
    palabras = texto.split()
    indices = [i for i in range(len(palabras)) if palabras[i].lower() == clave.lower()]
    bloques = []

    for pos in indices:
        inicio = pos - alcance if pos - alcance >= 0 else 0
        fin = pos + alcance + 1
        bloques.append(" ".join(palabras[inicio:fin]))

    return bloques

def analizar_documento(ruta, clave):
    total = 0
    with open(ruta, encoding='utf-8') as f:
        for num_linea, linea in enumerate(f, start=1):
            contexto = extraer_fragmentos(linea, clave)
            for fragmento in contexto:
                total += 1
                print(f"Línea {num_linea} => {fragmento}")
    
    print(f"\nNúmero total de veces que aparece '{clave}': {total}")

ruta_doc = 'documento.txt'
termino = input("Palabra clave: ")
analizar_documento(ruta_doc, termino)

