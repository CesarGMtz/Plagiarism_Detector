import string

def validadores():
    return {
        "longitud": lambda s: len(s) >= 8,
        "mayúsculas": lambda s: any(c.isupper() for c in s),
        "minúsculas": lambda s: any(c.islower() for c in s),
        "números": lambda s: any(c.isdigit() for c in s),
        "símbolos": lambda s: any(c in string.punctuation for c in s)
    }

def validar_clave(clave):
    reglas = validadores()
    fallos = [regla for regla, fn in reglas.items() if not fn(clave)]
    return fallos

def main():
    pwd = input("Escribe tu clave: ")
    errores = validar_clave(pwd)
    if errores:
        print("Contraseña inválida. Faltan:")
        for e in errores:
            print(f"- {e}")
    else:
        print("Clave fuerte y válida.")

main()

