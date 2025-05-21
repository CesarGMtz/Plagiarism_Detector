import string

def validar(cadena):
    es_valida = True
    mensajes = []

    if len(cadena) < 8:
        mensajes.append("Debe tener al menos 8 caracteres.")
        es_valida = False

    if not any(x.isupper() for x in cadena):
        mensajes.append("Debe incluir al menos una mayúscula.")
        es_valida = False

    if not any(x.islower() for x in cadena):
        mensajes.append("Debe incluir al menos una minúscula.")
        es_valida = False

    if not any(x.isdigit() for x in cadena):
        mensajes.append("Debe contener un número.")
        es_valida = False

    if not any(x in string.punctuation for x in cadena):
        mensajes.append("Debe incluir un carácter especial.")
        es_valida = False

    return es_valida, mensajes

def ejecutar():
    contra = input("Escribe tu contraseña: ")
    ok, detalles = validar(contra)

    if ok:
        print("Contraseña válida.")
    else:
        print("Errores:")
        for m in detalles:
            print("-", m)

ejecutar()
# Código para password_validator_1_tipo2.py
