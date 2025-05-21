import string

def checar_contraseña(pwd):
    condiciones = [
        ("longitud", lambda s: len(s) >= 8),
        ("mayúscula", lambda s: any(c.isupper() for c in s)),
        ("minúscula", lambda s: any(c.islower() for c in s)),
        ("número", lambda s: any(c.isdigit() for c in s)),
        ("símbolo", lambda s: any(c in string.punctuation for c in s))
    ]
    
    errores = [nombre for nombre, regla in condiciones if not regla(pwd)]
    return errores

def principal():
    clave = input("Clave a verificar: ")
    fallos = checar_contraseña(clave)
    if not fallos:
        print("Clave segura.")
    else:
        print("Faltan los siguientes requisitos:")
        for f in fallos:
            print(f"- {f}")

principal()

