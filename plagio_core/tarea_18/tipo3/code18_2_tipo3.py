def escanear_txt(nombre_archivo, termino):
    try:
        lineas = open(nombre_archivo, encoding='utf-8').readlines()
    except:
        print("Archivo no encontrado.")
        return

    info = [(i + 1, linea.strip()) for i, linea in enumerate(lineas) if termino.lower() in linea.lower()]
    
    print(f"'{termino}' aparece {len(info)} veces.")
    for linea_num, texto in info:
        print(f"[{linea_num}] {texto}")

doc = 'documento.txt'
clave = input("Término a escanear: ")
escanear_txt(doc, clave)

