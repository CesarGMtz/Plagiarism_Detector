def escanear_documento(ruta, objetivo):
    with open(ruta, encoding='utf-8') as entrada:
        contenido = entrada.readlines()

    coincidencias = []
    contador = 0
    linea_num = 1

    for texto in contenido:
        if objetivo.lower() in texto.lower():
            coincidencias.append((linea_num, texto.strip()))
            contador += 1
        linea_num += 1

    print(f"Palabra encontrada {contador} veces.")
    for elemento in coincidencias:
        print(f"[Línea {elemento[0]}] -> {elemento[1]}")

documento = 'documento.txt'
buscar = input("Palabra objetivo: ")
escanear_documento(documento, buscar)

