def es_simbolo_valido(c):
    return c.isdigit() or c in "+-*/(). "

def verificar_parentesis(expr):
    contador = 0
    for c in expr:
        if c == '(': contador += 1
        elif c == ')': contador -= 1
        if contador < 0: return False
    return contador == 0

def validar(expr):
    return all(es_simbolo_valido(c) for c in expr) and verificar_parentesis(expr)

def evaluar(expr):
    try:
        return eval(expr)
    except:
        return "No se pudo evaluar"

def principal():
    texto = input("Escribe una expresión: ")
    if validar(texto):
        print("Resultado:", evaluar(texto))
    else:
        print("Expresión inválida")

principal()

