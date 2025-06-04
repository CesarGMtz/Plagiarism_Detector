def crear():
    return [[" "]*3 for _ in range(3)]

def pintar(b):
    print("\n".join(" | ".join(fila) for fila in b))
    print()

def verificar(b, simb):
    lineas = b + list(zip(*b)) + [[b[i][i] for i in range(3)], [b[i][2 - i] for i in range(3)]]
    return any(all(c == simb for c in linea) for linea in lineas)

def jugar():
    b = crear()
    actual = "X"
    intentos = 0
    while intentos < 9:
        pintar(b)
        entrada = input(f"{actual} (formato 'fila,columna'): ")
        if "," not in entrada:
            print("Formato inválido.")
            continue
        fila, col = map(str.strip, entrada.split(","))
        if not fila.isdigit() or not col.isdigit():
            print("Solo números.")
            continue
        f, c = int(fila), int(col)
        if not (0 <= f < 3 and 0 <= c < 3):
            print("Fuera de rango.")
            continue
        if b[f][c] != " ":
            print("Ocupado.")
            continue
        b[f][c] = actual
        intentos += 1
        if verificar(b, actual):
            pintar(b)
            print(f"{actual} ha ganado.")
            return
        actual = "O" if actual == "X" else "X"
    pintar(b)
    print("¡Empate!")

jugar()

