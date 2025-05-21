def contexto_de_palabra(oracion, palabra, ventana=2):
    tokens = oracion.split()
    resultados = []
    for pos, tok in enumerate(tokens):
        if tok.lower() == palabra.lower():
            desde = max(0, pos - ventana)
            hasta = min(len(tokens), pos + ventana + 1)
            resultados.append(' '.join(tokens[desde:hasta]))
    return resultados

def buscar_en_archivo(ruta, clave):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        texto = archivo.readlines()

    apariciones = 0
    for i, linea in enumerate(texto, start=1):
        contexto = contexto_de_palabra(linea, clave)
        for c in contexto:
            apariciones += 1
            print(f"Línea {i}: {c}")

    print(f"\nTotal de veces encontrada la palabra '{clave}': {apariciones}")

doc = 'documento.txt'
buscar = input("Palabra clave a buscar: ")
buscar_en_archivo(doc, buscar)

