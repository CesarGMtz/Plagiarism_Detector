def iniciar_juego():
    tablero = {(i, j): " " for i in range(3) for j in range(3)}
    jugador = "X"
    for turno in range(9):
        mostrar(tablero)
        try:
            x, y = map(int, input(f"{jugador} elige posición (fila columna): ").split())
            if tablero[(x, y)] != " ":
                print("Ocupado. Intenta otra vez.")
                continue
            tablero[(x, y)] = jugador
            if ganador(tablero, jugador):
                mostrar(tablero)
                print(f"{jugador} ha ganado.")
                return
            jugador = "O" if jugador == "X" else "X"
        except:
            print("Entrada inválida.")
    mostrar(tablero)
    print("Empate.")

def mostrar(tab):
    for i in range(3):
        print(" | ".join(tab[(i, j)] for j in range(3)))
        if i < 2: print("--+---+--")

def ganador(tab, p):
    return any(all(tab[(i, j)] == p for j in range(3)) for i in range(3)) or \
           any(all(tab[(j, i)] == p for j in range(3)) for i in range(3)) or \
           all(tab[(i, i)] == p for i in range(3)) or \
           all(tab[(i, 2 - i)] == p for i in range(3))

iniciar_juego()

