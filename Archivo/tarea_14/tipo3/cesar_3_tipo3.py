def nuevo_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def tablero_lleno(tab):
    return all(cell != " " for fila in tab for cell in fila)

def mostrar(tab):
    for fila in tab:
        print(" | ".join(fila))
        print("-" * 5)

def evaluar(tab, p):
    for i in range(3):
        if all(tab[i][j] == p for j in range(3)) or all(tab[j][i] == p for j in range(3)):
            return True
    if all(tab[i][i] == p for i in range(3)) or all(tab[i][2 - i] == p for i in range(3)):
        return True
    return False

def juego():
    tablero = nuevo_tablero()
    jugadores = ["X", "O"]
    turno = 0

    while True:
        mostrar(tablero)
        actual = jugadores[turno % 2]
        print(f"Turno de {actual}")
        try:
            x = int(input("Fila: "))
            y = int(input("Columna: "))
        except ValueError:
            print("Entrada inválida.")
            continue
        if 0 <= x < 3 and 0 <= y < 3 and tablero[x][y] == " ":
            tablero[x][y] = actual
            if evaluar(tablero, actual):
                mostrar(tablero)
                print(f"¡{actual} gana!")
                break
            if tablero_lleno(tablero):
                mostrar(tablero)
                print("Empate.")
                break
            turno += 1
        else:
            print("Movimiento inválido")

juego()

