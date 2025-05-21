import re

def evaluar(pwd):
    errores = {}
    if len(pwd) < 8:
        errores["longitud"] = "Debe ser más larga."

    if not re.search(r"[A-Z]", pwd):
        errores["mayúscula"] = "No tiene letra mayúscula."

    if not re.search(r"[a-z]", pwd):
        errores["minúscula"] = "No tiene minúscula."

    if not re.search(r"\d", pwd):
        errores["número"] = "Falta número."

    if not re.search(r"[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?]", pwd):
        errores["símbolo"] = "Debe incluir símbolo."

    return errores

def run():
    pwd = input("Escribe tu contraseña: ")
    errores = evaluar(pwd)
    if not errores:
        print("Segura ✔️")
    else:
        print("Errores:")
        for e in errores.values():
            print("-", e)

run()

