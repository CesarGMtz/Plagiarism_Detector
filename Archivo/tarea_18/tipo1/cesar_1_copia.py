def buscar_palabra_contexto(archivo_txt, keyword, rango=3):
    with open(archivo_txt, 'r', encoding='utf-8') as file:
        contenido = file.readlines()

    cantidad = 0
    fragmentos = []

    for idx, linea in enumerate(contenido):
        if keyword in linea:
            cantidad += 1
            inicio = max(0, idx - rango)
            fin = min(len(contenido), idx + rango + 1)
            frag = contenido[inicio:fin]
            fragmentos.append(''.join(frag))

    print(f"La palabra '{keyword}' apareció {cantidad} veces.")
    for n, texto in enumerate(fragmentos, 1):
        print(f"\n--- Fragmento {n} ---\n{texto}")

ruta = 'documento.txt'
clave = input("Palabra clave: ")
buscar_palabra_contexto(ruta, clave)

