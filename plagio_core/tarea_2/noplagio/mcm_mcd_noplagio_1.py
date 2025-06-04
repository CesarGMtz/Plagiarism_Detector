print("Herramienta para calcular MCD y MCM")

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

x, y = a, b
while y:
    x, y = y, x % y
mcd = x

# Definir MCM usando una lambda
calcular_mcm = lambda n1, n2, mcd_val: abs(n1 * n2) // mcd_val
mcm = calcular_mcm(a, b, mcd)

print("Resultado:")
print(f"MCD({a}, {b}) = {mcd}")
print(f"MCM({a}, {b}) = {mcm}")