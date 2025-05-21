import string

class Validador:
    def __init__(self, texto):
        self.texto = texto

    def contiene_letra(self):
        return any(c.isalpha() for c in self.texto)

    def contiene_numero(self):
        return any(c.isdigit() for c in self.texto)

    def contiene_simbolo(self):
        return any(c in string.punctuation for c in self.texto)

    def longitud_correcta(self):
        return len(self.texto) >= 8

    def es_valida(self):
        return (self.longitud_correcta() and
                self.contiene_letra() and
                self.contiene_numero() and
                self.contiene_simbolo())

    def errores(self):
        errores = []
        if not self.longitud_correcta():
            errores.append("Mínimo 8 caracteres.")
        if not self.contiene_letra():
            errores.append("Debe incluir letras.")
        if not self.contiene_numero():
            errores.append("Debe incluir números.")
        if not self.contiene_simbolo():
            errores.append("Debe incluir símbolos.")
        return errores

def ejecutar_validador():
    while True:
        entrada = input("Introduce una contraseña: ")
        v = Validador(entrada)
        if v.es_valida():
            print("Contraseña válida.")
            break
        else:
            print("Errores:")
            for e in v.errores():
                print("-", e)

ejecutar_validador()

