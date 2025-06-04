def agenda():
    contactos = []

    def insertar():
        nombre = input("Nombre: ")
        tel = input("Tel: ")
        contactos.append((nombre, tel))
        print("Guardado.")

    def consultar():
        n = input("Buscar: ")
        encontrados = [f"{x[0]}: {x[1]}" for x in contactos if x[0] == n]
        print(encontrados[0] if encontrados else "No encontrado.")

    def listar():
        if not contactos:
            print("Vacío.")
        for c in contactos:
            print(f"{c[0]} -> {c[1]}")

    while True:
        print("\n1.Añadir 2.Buscar 3.Ver todo 4.Salir")
        op = input("Opción: ")
        if op == "1": insertar()
        elif op == "2": consultar()
        elif op == "3": listar()
        elif op == "4": break
        else: print("Inválido")

agenda()

