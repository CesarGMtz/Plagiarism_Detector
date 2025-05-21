import re

def analizar_contraseña(pwd):
    errores = {}
    if len(pwd) < 8:
        errores["longitud"] = "Muy corta."

    if not re.search(r"[A-Z]", pwd):
        errores["mayus"] = "Falta mayúscula."

    if not re.search(r"[a-z]", pwd):
        errores["minus"] = "Falta minúscula."

    if not re.search(r"\d", pwd):
        errores["digito"] = "Falta número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        errores["simbolo"] = "Falta símbolo."

    return errores

def revisar():
    pwd = input("Introduce la contraseña a validar: ")
    fallas = analizar_contraseña(pwd)
    if not fallas:
        print("Contraseña válida.")
    else:
        print("Errores detectados:")
        for clave, valor in fallas.items():
            print(f"- {clave}: {valor}")

revisar()

