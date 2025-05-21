class Conversor:
    def __init__(self, numero):
        self.numero = numero

    def a_binario(self):
        return format(self.numero, 'b')

    def a_octal(self):
        return format(self.numero, 'o')

    def a_hexadecimal(self):
        return format(self.numero, 'X')

def main():
    print("=== Conversor Decimal a otras bases ===")
    try:
        n = int(input("Introduce un número: "))
        if n < 0:
            print("Número no válido.")
            return
        conv = Conversor(n)
        print("Binario:", conv.a_binario())
        print("Octal:", conv.a_octal())
        print("Hexadecimal:", conv.a_hexadecimal())
    except:
        print("Dato inválido.")

main()