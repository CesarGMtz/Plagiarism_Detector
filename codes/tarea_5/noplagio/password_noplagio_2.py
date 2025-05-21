import string

def mostrar_requisitos():
    print("Requisitos de contraseña segura:")
    print("- Mínimo 8 caracteres")
    print("- Al menos una letra mayúscula")
    print("- Al menos una letra minúscula")
    print("- Al menos un número")
    print("- Al menos un símbolo (!, @, #, etc.)\n")

def pedir_contraseña():
    return input("Introduce tu contraseña para validar: ")

def cumple_todo(texto):
    return all([
        len(texto) >= 8,
        any(c.isupper() for c in texto),
        any(c.islower() for c in texto),
        any(c.isdigit() for c in texto),
        any(c in string.punctuation for c in texto)
    ])

def programa():
    mostrar_requisitos()
    clave = pedir_contraseña()
    if cumple_todo(clave):
        print("✔ Contraseña aceptada.")
    else:
        print("❌ Contraseña no cumple con todos los requisitos.")

programa()

