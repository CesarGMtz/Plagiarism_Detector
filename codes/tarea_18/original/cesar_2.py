def buscar_palabra_con_contexto(ruta, palabra_clave, contexto=3):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    ocurrencias = 0
    resultados = []

    for i, linea in enumerate(lineas):
        if palabra_clave in linea:
            ocurrencias += 1
            inicio = max(0, i - contexto)
            fin = min(len(lineas), i + contexto + 1)
            contexto_lineas = lineas[inicio:fin]
            resultados.append(''.join(contexto_lineas))

    print(f"Se encontró '{palabra_clave}' {ocurrencias} veces.\n")
    for i, fragmento in enumerate(resultados, 1):
        print(f"--- Contexto {i} ---\n{fragmento}\n")

ruta_archivo = 'documento.txt'
palabra = input("Introduce la palabra clave a buscar: ")
buscar_palabra_con_contexto(ruta_archivo, palabra)

