def imprimir_cuadro(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def hay_ganador(tab, j):
    for i in range(3):
        if all(tab[i][x] == j for x in range(3)):
            return True
    for i in range(3):
        if all(tab[x][i] == j for x in range(3)):
            return True
    if all(tab[i][i] == j for i in range(3)) or all(tab[i][2 - i] == j for i in range(3)):
        return True
    return False

tablero = [[" "] * 3 for _ in range(3)]
actual = "X"
contador = 0

while contador < 9:
    imprimir_cuadro(tablero)
    fila, columna = map(int, input(f"{actual} -> Ingresa fila columna: ").split())
    if tablero[fila][columna] != " ":
        print("Ya hay una jugada ahí.")
        continue
    tablero[fila][columna] = actual
    contador += 1
    if hay_ganador(tablero, actual):
        imprimir_cuadro(tablero)
        print(f"Jugador {actual} gana.")
        break
    actual = "O" if actual == "X" else "X"
else:
    imprimir_cuadro(tablero)
    print("¡Juego empatado!")

