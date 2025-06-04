def mostrar_tablero(matriz):
    for fila in matriz:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(matriz, simbolo):
    filas = any(all(c == simbolo for c in fila) for fila in matriz)
    columnas = any(all(matriz[f][col] == simbolo for f in range(3)) for col in range(3))
    diagonal_p = all(matriz[k][k] == simbolo for k in range(3))
    diagonal_s = all(matriz[k][2 - k] == simbolo for k in range(3))
    return filas or columnas or diagonal_p or diagonal_s

def jugar():
    tablero = [[" "] * 3 for _ in range(3)]
    turno = "X"
    jugadas = 0

    while jugadas < 9:
        mostrar_tablero(tablero)
        try:
            fila, col = map(int, input(f"Turno de {turno}: ").split())
            if tablero[fila][col] != " ":
                print("Esa casilla ya está ocupada.")
                continue
            tablero[fila][col] = turno
            jugadas += 1
            if verificar_ganador(tablero, turno):
                mostrar_tablero(tablero)
                print(f"¡{turno} ha ganado!")
                return
            turno = "O" if turno == "X" else "X"
        except:
            print("Entrada inválida. Usa dos números separados por espacio.")

    mostrar_tablero(tablero)
    print("Empate")

jugar()

