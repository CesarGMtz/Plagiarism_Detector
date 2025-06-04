import string

class ValidadorContraseña:
    def __init__(self, pwd):
        self.pwd = pwd

    def es_fuerte(self):
        if len(self.pwd) < 8:
            return False, "Debe tener mínimo 8 caracteres."
        if not any(c.isupper() for c in self.pwd):
            return False, "Debe incluir una mayúscula."
        if not any(c.islower() for c in self.pwd):
            return False, "Debe incluir una minúscula."
        if not any(c.isdigit() for c in self.pwd):
            return False, "Debe tener un número."
        if not any(c in string.punctuation for c in self.pwd):
            return False, "Debe contener un símbolo."
        return True, "Contraseña segura."

def iniciar():
    entrada = input("Contraseña: ")
    validador = ValidadorContraseña(entrada)
    valido, resultado = validador.es_fuerte()
    print(resultado)

iniciar()

