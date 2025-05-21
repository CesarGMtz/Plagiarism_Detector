datos = {}

def procesar(entrada):
    if entrada == "1":
        nom, tel = input("Nombre: "), input("Tel: ")
        datos[nom] = tel
        print("✓ Guardado")
    elif entrada == "2":
        nom = input("Buscar: ")
        print(f"{nom}: {datos.get(nom, 'No hallado')}")
    elif entrada == "3":
        print("\n".join([f"{n}: {t}" for n, t in datos.items()]) or "Sin datos.")
    elif entrada != "4":
        print("Opción incorrecta")

def opciones():
    print("1) Agregar\n2) Buscar\n3) Mostrar\n4) Salir")

while True:
    opciones()
    eleccion = input("Elige opción: ")
    if eleccion == "4":
        break
    procesar(eleccion)

