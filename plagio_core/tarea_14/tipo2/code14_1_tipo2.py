def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def ganador(tablero, simbolo):
    for i in range(3):
        if all(celda == simbolo for celda in tablero[i]) or \
           all(tablero[j][i] == simbolo for j in range(3)):
            return True
    return (tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo or
            tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo)

def jugar_gato():
    tablero = [[" "] * 3 for _ in range(3)]
    turno = "X"

    for _ in range(9):
        mostrar_tablero(tablero)
        try:
            fila, col = map(int, input(f"Turno de {turno} (fila columna): ").split())
            if tablero[fila][col] != " ":
                print("Casilla ocupada. Intenta de nuevo.")
                continue
            tablero[fila][col] = turno
            if ganador(tablero, turno):
                mostrar_tablero(tablero)
                print(f"¡{turno} ha ganado!")
                return
            turno = "O" if turno == "X" else "X"
        except:
            print("Entrada inválida. Usa dos números separados por espacio.")

    mostrar_tablero(tablero)
    print("¡Empate!")

jugar_gato()

