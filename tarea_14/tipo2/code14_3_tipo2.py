tablero = [[" " for _ in range(3)] for _ in range(3)]

def mostrar():
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def ha_ganado(simbolo):
    for i in range(3):
        if tablero[i] == [simbolo] * 3 or [tablero[j][i] for j in range(3)] == [simbolo] * 3:
            return True
    return (tablero[0][0] == simbolo == tablero[1][1] == tablero[2][2] or
            tablero[0][2] == simbolo == tablero[1][1] == tablero[2][0])

rondas = 0
jugador = "X"

while rondas < 9:
    mostrar()
    try:
        fila, columna = map(int, input(f"Turno de {jugador}, elige fila y columna: ").split())
        if tablero[fila][columna] != " ":
            print("Casilla ocupada, intenta de nuevo.")
            continue
        tablero[fila][columna] = jugador
        if ha_ganado(jugador):
            mostrar()
            print(f"¡{jugador} gana!")
            break
        jugador = "O" if jugador == "X" else "X"
        rondas += 1
    except:
        print("Entrada inválida. Usa dos números separados por espacio.")
else:
    mostrar()
    print("¡Empate!")

