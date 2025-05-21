def buscar_y_contar_palabra(ruta_archivo, palabra):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()

    conteo = 0
    coincidencias = []

    for indice, linea in enumerate(contenido, 1):
        if palabra.lower() in linea.lower():
            conteo += 1
            coincidencias.append((indice, linea.strip()))

    print(f"'{palabra}' aparece {conteo} veces.")
    for numero, linea in coincidencias:
        print(f"Línea {numero}: {linea}")

archivo = 'documento.txt'
clave = input("Palabra a buscar: ")
buscar_y_contar_palabra(archivo, clave)

