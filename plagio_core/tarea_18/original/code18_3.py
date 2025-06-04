def obtener_contexto_palabras(linea, palabra, ventana=2):
    palabras = linea.split()
    contexto = []
    for i, p in enumerate(palabras):
        if p.lower() == palabra.lower():
            inicio = max(i - ventana, 0)
            fin = min(i + ventana + 1, len(palabras))
            contexto.append(' '.join(palabras[inicio:fin]))
    return contexto

def buscar_contexto_en_archivo(ruta, palabra_clave):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    total = 0
    for num, linea in enumerate(lineas, 1):
        fragmentos = obtener_contexto_palabras(linea, palabra_clave)
        for frag in fragmentos:
            total += 1
            print(f"Línea {num}: {frag}")

    print(f"\nTotal de ocurrencias de '{palabra_clave}': {total}")

archivo = 'documento.txt'
clave = input("Introduce palabra clave: ")
buscar_contexto_en_archivo(archivo, clave)

