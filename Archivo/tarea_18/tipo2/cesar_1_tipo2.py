def obtener_contexto(ruta_archivo, palabra, margen=3):
    archivo = open(ruta_archivo, encoding='utf-8')
    lineas_totales = archivo.readlines()
    archivo.close()

    resultados = []
    total = 0

    for linea_actual in range(len(lineas_totales)):
        if palabra in lineas_totales[linea_actual]:
            total += 1
            desde = linea_actual - margen if linea_actual - margen >= 0 else 0
            hasta = linea_actual + margen + 1
            resultados.append("".join(lineas_totales[desde:hasta]))

    print(f"Ocurrencias encontradas: {total}")
    for i in range(len(resultados)):
        print(f"\n>> Resultado {i + 1}:\n{resultados[i]}")
        
archivo = 'documento.txt'
clave = input("¿Qué palabra deseas encontrar?: ")
obtener_contexto(archivo, clave)

