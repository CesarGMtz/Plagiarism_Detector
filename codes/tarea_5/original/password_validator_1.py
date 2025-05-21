import string

def validar_contraseña(pwd):
    if len(pwd) < 8:
        return False, "Debe tener al menos 8 caracteres."

    tiene_mayus = any(c.isupper() for c in pwd)
    tiene_minus = any(c.islower() for c in pwd)
    tiene_digito = any(c.isdigit() for c in pwd)
    tiene_simbolo = any(c in string.punctuation for c in pwd)

    if not tiene_mayus:
        return False, "Debe tener al menos una letra mayúscula."
    if not tiene_minus:
        return False, "Debe tener al menos una letra minúscula."
    if not tiene_digito:
        return False, "Debe tener al menos un número."
    if not tiene_simbolo:
        return False, "Debe tener al menos un símbolo especial."

    return True, "Contraseña válida."

def main():
    pwd = input("Ingresa tu contraseña: ")
    valida, mensaje = validar_contraseña(pwd)
    print(mensaje)

main()

