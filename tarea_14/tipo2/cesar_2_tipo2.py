def crear_tablero():
    return [" "] * 9

def imprimir_tablero(t):
    for i in range(0, 9, 3):
        print(" | ".join(t[i:i+3]))
        if i < 6: print("---------")

def verificar_lineas(t, p):
    for i in range(3):
        if t[i*3:i*3+3] == [p]*3:
            return True
        if [t[i], t[i+3], t[i+6]] == [p]*3:
            return True
    return [t[0], t[4], t[8]] == [p]*3 or [t[2], t[4], t[6]] == [p]*3

def juego():
    t = crear_tablero()
    j = "X"
    for m in range(9):
        imprimir_tablero(t)
        pos = int(input(f"Turno de {j} (0-8): "))
        if t[pos] != " ":
            print("Ocupado. Reintenta.")
            continue
        t[pos] = j
        if verificar_lineas(t, j):
            imprimir_tablero(t)
            print(f"¡{j} gana!")
            return
        j = "O" if j == "X" else "X"
    imprimir_tablero(t)
    print("Empate")

juego()

