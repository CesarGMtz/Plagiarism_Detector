import string

def tiene_longitud_valida(pwd):
    return len(pwd) >= 8

def tiene_letras_y_digitos(pwd):
    letras = any(c.isalpha() for c in pwd)
    digitos = any(c.isdigit() for c in pwd)
    return letras and digitos

def tiene_caracter_especial(pwd):
    return any(c in string.punctuation for c in pwd)

def validar(pwd):
    if not tiene_longitud_valida(pwd):
        return "Demasiado corta"
    if not tiene_letras_y_digitos(pwd):
        return "Debe tener letras y dígitos"
    if not tiene_caracter_especial(pwd):
        return "Debe incluir un símbolo"
    return "Contraseña válida"

def solicitar_contraseña():
    return input("Ingresa tu contraseña: ")

def flujo():
    while True:
        pwd = solicitar_contraseña()
        resultado = validar(pwd)
        print("Resultado:", resultado)
        if resultado == "Contraseña válida":
            break

flujo()

