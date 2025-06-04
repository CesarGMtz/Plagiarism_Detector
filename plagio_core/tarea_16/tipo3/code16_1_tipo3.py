contactos = {}

def procesar_comando(cmd):
    if cmd.startswith("agregar"):
        try:
            _, nombre, numero = cmd.split()
            contactos[nombre] = numero
            print("Contacto agregado.")
        except:
            print("Uso: agregar <nombre> <telefono>")
    elif cmd.startswith("buscar"):
        try:
            _, nombre = cmd.split()
            print(f"{nombre}: {contactos[nombre]}" if nombre in contactos else "No encontrado.")
        except:
            print("Uso: buscar <nombre>")
    elif cmd == "mostrar":
        if contactos:
            for c in contactos:
                print(f"{c} => {contactos[c]}")
        else:
            print("Agenda vacía.")
    else:
        print("Comando inválido.")

print("Comandos: agregar <nombre> <tel>, buscar <nombre>, mostrar, salir")
while True:
    entrada = input(">> ")
    if entrada == "salir":
        break
    procesar_comando(entrada)

