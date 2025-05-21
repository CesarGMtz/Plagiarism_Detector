import numpy as np
import matplotlib.pyplot as plt

print("Graficador de funciones")
print("Por ejemplo: x**3 - 2*x + 1")
form = input("Escribe la fórmula: ")

x_data = np.linspace(-10, 10, 600)
y_data = []

for x in x_data:
    try:
        y = eval(form)
    except:
        y = float("nan")
    y_data.append(y)

plt.figure()
plt.plot(x_data, y_data)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica generada")
plt.grid()
plt.show()

