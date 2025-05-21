agenda = {}

print("Comandos válidos:")
print("nuevo <nombre> <telefono>")
print("ver <nombre>")
print("todos")
print("fin")

while True:
    entrada = input(">> ").strip()
    if entrada == "fin":
        break
    elif entrada.startswith("nuevo"):
        partes = entrada.split()
        if len(partes) == 3:
            _, nombre, tel = partes
            agenda[nombre] = tel
            print("Contacto creado.")
        else:
            print("Formato: nuevo <nombre> <telefono>")
    elif entrada.startswith("ver"):
        partes = entrada.split()
        if len(partes) == 2:
            print(agenda.get(partes[1], "No encontrado"))
        else:
            print("Formato: ver <nombre>")
    elif entrada == "todos":
        for k, v in agenda.items():
            print(f"{k}: {v}")
    else:
        print("Comando desconocido.")

