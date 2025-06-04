import string

def revisar_password(clave):
    if len(clave) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."

    tiene_M = any(letra.isupper() for letra in clave)
    tiene_m = any(letra.islower() for letra in clave)
    tiene_num = any(c.isdigit() for c in clave)
    tiene_esp = any(c in string.punctuation for c in clave)

    if not tiene_M:
        return False, "Se necesita una mayúscula."
    if not tiene_m:
        return False, "Se necesita una minúscula."
    if not tiene_num:
        return False, "Debe contener un número."
    if not tiene_esp:
        return False, "Falta símbolo especial."

    return True, "Clave válida."

def iniciar():
    clave = input("Introduce contraseña: ")
    ok, msg = revisar_password(clave)
    print(msg)

iniciar()

