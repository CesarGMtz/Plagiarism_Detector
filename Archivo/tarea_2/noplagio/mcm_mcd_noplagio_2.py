class Calculadora:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2

    def mcd(self):
        a, b = self.a, self.b
        while b:
            a, b = b, a % b
        return a

    def mcm(self):
        return abs(self.a * self.b) // self.mcd()

print("Cálculo con clases: MCD y MCM")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
calc = Calculadora(n1, n2)

print("MCD:", calc.mcd())
print("MCM:", calc.mcm())