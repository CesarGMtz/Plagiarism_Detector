import string

def verificar_segura(palabra):
    if len(palabra) < 8:
        raise ValueError("Muy corta (mínimo 8 caracteres).")
    if not any(l.isupper() for l in palabra):
        raise ValueError("Falta una mayúscula.")
    if not any(l.islower() for l in palabra):
        raise ValueError("Falta una minúscula.")
    if not any(l.isdigit() for l in palabra):
        raise ValueError("Debe incluir un número.")
    if not any(l in string.punctuation for l in palabra):
        raise ValueError("Falta símbolo especial.")
    return True

def validar_interactivo():
    try:
        clave = input("Contraseña a validar: ")
        if verificar_segura(clave):
            print("✔ Contraseña válida.")
    except ValueError as e:
        print("Error:", str(e))

validar_interactivo()

