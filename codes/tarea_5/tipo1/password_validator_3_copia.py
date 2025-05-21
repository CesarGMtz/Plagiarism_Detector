import string

class RevisorClave:
    def __init__(self, clave):
        self.clave = clave

    def comprobar(self):
        if len(self.clave) < 8:
            return False, "Muy corta (mínimo 8)."
        if not any(c.isupper() for c in self.clave):
            return False, "Debe tener mayúscula."
        if not any(c.islower() for c in self.clave):
            return False, "Falta minúscula."
        if not any(c.isdigit() for c in self.clave):
            return False, "Requiere número."
        if not any(c in string.punctuation for c in self.clave):
            return False, "No hay símbolo."
        return True, "Contraseña válida."

def validar():
    clave = input("Ingresa clave: ")
    rev = RevisorClave(clave)
    estado, mensaje = rev.comprobar()
    print(mensaje)

validar()

