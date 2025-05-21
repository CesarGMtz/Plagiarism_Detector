def buscar_clave_contexto(path, clave, margen=3):
    with open(path, encoding='utf-8') as f:
        texto = f.read().split('\n')

    posiciones = [i for i, l in enumerate(texto) if clave in l]
    resultados = []

    for idx in posiciones:
        contexto = texto[max(0, idx - margen): idx + margen + 1]
        resultados.append('\n'.join(contexto))

    print(f"La palabra '{clave}' fue encontrada {len(posiciones)} veces.")
    print("\n".join([f"\n>> Contexto {i+1}:\n{res}" for i, res in enumerate(resultados)]))

archivo = 'documento.txt'
clave = input("Palabra a buscar: ")
buscar_clave_contexto(archivo, clave)

