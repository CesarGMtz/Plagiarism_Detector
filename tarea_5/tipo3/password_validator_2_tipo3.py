import re

def validar_longitud(pwd):
    return len(pwd) >= 8

def validar_patrones(pwd):
    return {
        "mayúscula": bool(re.search(r"[A-Z]", pwd)),
        "minúscula": bool(re.search(r"[a-z]", pwd)),
        "dígito": bool(re.search(r"[0-9]", pwd)),
        "especial": bool(re.search(r"[!@#$%^&*()_+=]", pwd))
    }

def validar_todo(pwd):
    errores = []
    if not validar_longitud(pwd):
        errores.append("Debe tener al menos 8 caracteres")
    patrones = validar_patrones(pwd)
    for k, v in patrones.items():
        if not v:
            errores.append(f"Debe contener una {k}")
    return errores

def entrada_usuario():
    return input("Escribe una contraseña para validar: ")

def iniciar():
    while True:
        pwd = entrada_usuario()
        errores = validar_todo(pwd)
        if not errores:
            print("Contraseña válida ✅")
            break
        else:
            print("Errores:")
            for e in errores:
                print("-", e)

iniciar()

