import random
import string

def generar_segura(tamaño):
    if tamaño < 6:
        raise ValueError("Longitud demasiado corta")
    
    partes = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    resto = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=tamaño - len(partes)))
    completa = partes + list(resto)
    random.shuffle(completa)
    return ''.join(completa)

def sin_repetidas(cantidad, tamaño):
    resultado = []
    while len(resultado) < cantidad:
        nueva = generar_segura(tamaño)
        if nueva not in resultado:
            resultado.append(nueva)
    return resultado

def main():
    n = int(input("¿Cuántas deseas? "))
    l = int(input("Longitud: "))
    claves = sin_repetidas(n, l)
    print("\nLista final:")
    for c in claves:
        print(c)

main()

