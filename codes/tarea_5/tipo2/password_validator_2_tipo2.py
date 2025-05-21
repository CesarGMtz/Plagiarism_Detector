import re

def tiene_mayus(p): return re.search(r"[A-Z]", p)
def tiene_minus(p): return re.search(r"[a-z]", p)
def tiene_num(p): return re.search(r"[0-9]", p)
def tiene_symbolo(p): return re.search(r"[^\w\s]", p)
def longitud_ok(p): return len(p) >= 8

def revisar_pwd(p):
    reglas = [
        (longitud_ok(p), "Mínimo 8 caracteres."),
        (tiene_mayus(p), "Una mayúscula requerida."),
        (tiene_minus(p), "Debe incluir una minúscula."),
        (tiene_num(p), "Debe contener números."),
        (tiene_symbolo(p), "Falta símbolo especial.")
    ]
    return [msg for cond, msg in reglas if not cond]

def inicio():
    clave = input("Introduce la contraseña: ")
    fallas = revisar_pwd(clave)

    if not fallas:
        print("Todo correcto.")
    else:
        print("Revisa los siguientes requisitos:")
        for fallo in fallas:
            print(f"- {fallo}")

inicio()

