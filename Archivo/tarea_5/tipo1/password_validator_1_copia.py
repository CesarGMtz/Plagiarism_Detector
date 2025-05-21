import string

def verificar_pwd(palabra):
    if len(palabra) < 8:
        return False, "Longitud insuficiente."

    mayus = any(l.isupper() for l in palabra)
    minus = any(l.islower() for l in palabra)
    num = any(l.isdigit() for l in palabra)
    simbolo = any(l in string.punctuation for l in palabra)

    if not mayus:
        return False, "Agrega una letra en mayúscula."
    if not minus:
        return False, "Se necesita al menos una minúscula."
    if not num:
        return False, "Incluye un número."
    if not simbolo:
        return False, "Debe contener un símbolo."

    return True, "Contraseña válida."

def inicio():
    entrada = input("Introduce una contraseña: ")
    ok, msj = verificar_pwd(entrada)
    print(msj)

inicio()

