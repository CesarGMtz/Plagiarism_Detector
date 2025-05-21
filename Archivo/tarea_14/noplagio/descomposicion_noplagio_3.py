def crear_tablero():
    return [[" "]*3 for _ in range(3)]

def mostrar(tablero):
    print("  A B C")
    for i, fila in enumerate(tablero):
        print(f"{i+1} " + " ".join(fila))

def mover(tablero, pos, jugador):
    columnas = {'A': 0, 'B': 1, 'C': 2}
    filas = {'1': 0, '2': 1, '3': 2}
    if len(pos) != 2 or pos[0] not in columnas or pos[1] not in filas:
        return False
    x, y = filas[pos[1]], columnas[pos[0]]
    if tablero[x][y] != " ":
        return False
    tablero[x][y] = jugador
    return True

def hay_ganador(t, j):
    return any(all(c == j for c in fila) for fila in t) or \
           any(all(t[i][j] == j for i in range(3)) for j in range(3)) or \
           all(t[i][i] == j for i in range(3)) or \
           all(t[i][2 - i] == j for i in range(3))

def main():
    t = crear_tablero()
    turno = "X"
    for _ in range(9):
        mostrar(t)
        pos = input(f"{turno} juega (ej: A1): ").upper()
        if not mover(t, pos, turno):
            print("Movimiento inválido.")
            continue
        if hay_ganador(t, turno):
            mostrar(t)
            print(f"{turno} gana!")
            return
        turno = "O" if turno == "X" else "X"
    mostrar(t)
    print("Empate")

main()

