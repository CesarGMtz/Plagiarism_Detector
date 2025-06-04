def mostrar_tablero(t):
    print(f"\n{t[0]} | {t[1]} | {t[2]}")
    print("--+---+--")
    print(f"{t[3]} | {t[4]} | {t[5]}")
    print("--+---+--")
    print(f"{t[6]} | {t[7]} | {t[8]}\n")

def ganador(t, j):
    combinaciones = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
                     (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(t[a]==t[b]==t[c]==j for a,b,c in combinaciones)

def jugar():
    tablero = [" "] * 9
    jugador = "X"
    for _ in range(9):
        mostrar_tablero(tablero)
        p = int(input(f"{jugador} elige casilla (1-9): ")) - 1
        if tablero[p] != " ":
            print("Casilla ocupada.")
            continue
        tablero[p] = jugador
        if ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"{jugador} gana.")
            return
        jugador = "O" if jugador == "X" else "X"
    mostrar_tablero(tablero)
    print("Empate")

jugar()

