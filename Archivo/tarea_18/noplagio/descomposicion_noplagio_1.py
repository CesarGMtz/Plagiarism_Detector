import re

def buscar_clave_regex(path, clave, contexto=3):
    with open(path, 'r', encoding='utf-8') as f:
        contenido = f.readlines()

    contexto_dict = {}
    total = 0
    patron = re.compile(r'\b' + re.escape(clave) + r'\b', re.IGNORECASE)

    for i in range(len(contenido)):
        if patron.search(contenido[i]):
            total += 1
            contexto_dict[i] = contenido[max(0, i-contexto):min(len(contenido), i+contexto+1)]

    print(f"Ocurrencias de '{clave}': {total}\n")
    for idx, frag in contexto_dict.items():
        print(f"== Contexto línea {idx+1} ==\n{''.join(frag)}")

archivo = 'documento.txt'
clave = input("Palabra clave: ")
buscar_clave_regex(archivo, clave)

