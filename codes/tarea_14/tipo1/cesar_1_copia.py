def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def revisar_ganador(tablero, jugador):
    for i in range(3):
        if all([x == jugador for x in tablero[i]]) or \
           all([tablero[j][i] == jugador for j in range(3)]):
            return True
    return tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
           tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador

def juego():
    tablero = [[" "] * 3 for _ in range(3)]
    jugador = "X"
    for _ in range(9):
        mostrar_tablero(tablero)
        fila, col = map(int, input(f"{jugador} juega (fila columna): ").split())
        if tablero[fila][col] != " ":
            print("Lugar ocupado, intenta otra vez.")
            continue
        tablero[fila][col] = jugador
        if revisar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"¡{jugador} ha ganado!")
            return
        jugador = "O" if jugador == "X" else "X"
    print("Empate")
    mostrar_tablero(tablero)

juego()

