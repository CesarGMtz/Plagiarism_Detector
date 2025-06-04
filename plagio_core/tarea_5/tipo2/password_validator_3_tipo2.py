import string

class RevisorClave:
    def __init__(self, texto):
        self.texto = texto

    def validar(self):
        if len(self.texto) < 8:
            return False, "Debe contener al menos 8 caracteres."
        if not any(c.isupper() for c in self.texto):
            return False, "Falta una letra en mayúscula."
        if not any(c.islower() for c in self.texto):
            return False, "Falta una letra en minúscula."
        if not any(c.isdigit() for c in self.texto):
            return False, "Debe incluir un número."
        if not any(c in string.punctuation for c in self.texto):
            return False, "Se requiere un símbolo especial."
        return True, "Clave aceptada."

def ejecutar():
    clave = input("Ingresa tu contraseña: ")
    revisor = RevisorClave(clave)
    ok, mensaje = revisor.validar()
    print(mensaje)

ejecutar()

