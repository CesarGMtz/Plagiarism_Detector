def encontrar_con_contexto(archivo, termino, margen=3):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.readlines()

    coincidencias = 0
    fragmentos = []

    for i, linea in enumerate(contenido):
        if termino in linea:
            coincidencias += 1
            inicio = max(0, i - margen)
            fin = min(len(contenido), i + margen + 1)
            fragmento = ''.join(contenido[inicio:fin])
            fragmentos.append(fragmento)

    print(f"\n'{termino}' fue encontrado {coincidencias} veces.\n")
    for idx, bloque in enumerate(fragmentos, 1):
        print(f"=== Fragmento {idx} ===\n{bloque}")

ruta = 'documento.txt'
clave = input("Palabra a buscar: ")
encontrar_con_contexto(ruta, clave)

