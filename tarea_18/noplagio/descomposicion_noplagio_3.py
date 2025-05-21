def stream_busqueda(archivo, clave, contexto=2):
    buffer = []
    total = 0

    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    for i in range(len(lineas)):
        if clave.lower() in lineas[i].lower():
            total += 1
            desde = max(0, i - contexto)
            hasta = min(len(lineas), i + contexto + 1)
            fragmento = ''.join(lineas[desde:hasta])
            buffer.append(fragmento)

    print(f"'{clave}' se encontró {total} veces.")
    for idx, texto in enumerate(buffer):
        print(f"\n>> Fragmento {idx+1}:\n{texto}")

archivo = 'documento.txt'
palabra = input("Buscar palabra clave: ")
stream_busqueda(archivo, palabra)

