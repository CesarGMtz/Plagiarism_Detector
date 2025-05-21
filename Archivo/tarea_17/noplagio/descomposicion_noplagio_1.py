from sympy import symbols, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
expresion = input("Introduce una función (ej: sin(x) + x**2): ")

try:
    funcion = sympify(expresion)
    f_lamb = lambdify(x, funcion, modules=['numpy'])
    x_vals = np.linspace(-10, 10, 500)
    y_vals = f_lamb(x_vals)

    plt.plot(x_vals, y_vals)
    plt.title(f"Función: {expresion}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()
except Exception as e:
    print("Expresión inválida:", e)

