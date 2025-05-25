import re

def validar_clave(clave):
    errores = {}
    if len(clave) < 8:
        errores["longitud"] = "Debe tener al menos 8 caracteres."

    if not re.search(r"[A-Z]", clave):
        errores["mayúscula"] = "Falta al menos una letra en mayúscula."

    if not re.search(r"[a-z]", clave):
        errores["minúscula"] = "Falta al menos una letra en minúscula."

    if not re.search(r"\d", clave):
        errores["número"] = "Debe contener un dígito."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", clave):
        errores["símbolo"] = "Debe incluir un símbolo especial."

    return errores

def ejecutar():
    entrada = input("Escribe una contraseña: ")
    problemas = validar_clave(entrada)

    if not problemas:
        print("La contraseña es segura.")
    else:
        print("Errores:")
        for campo, mensaje in problemas.items():
            print(f"- {campo}: {mensaje}")

ejecutar()

