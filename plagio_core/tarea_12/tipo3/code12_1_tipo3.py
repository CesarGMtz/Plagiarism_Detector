import random
import string

class GeneradorContraseñas:
    def __init__(self, longitud=12):
        self.longitud = longitud
        self.caracteres = string.ascii_letters + string.digits + string.punctuation

    def crear(self):
        return ''.join(random.choices(self.caracteres, k=self.longitud))

    def generar_unicas(self, cantidad):
        resultado = set()
        while len(resultado) < cantidad:
            resultado.add(self.crear())
        return list(resultado)

def main():
    g = GeneradorContraseñas()
    num = int(input("Cuántas contraseñas deseas generar: "))
    lista = g.generar_unicas(num)
    print("\nLista generada:")
    for i, c in enumerate(lista):
        print(f"{i+1}: {c}")

if __name__ == "__main__":
    main()

