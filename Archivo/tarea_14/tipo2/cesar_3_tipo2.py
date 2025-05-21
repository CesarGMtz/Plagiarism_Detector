def crear_matriz():
    return [[" "]*3 for _ in range(3)]

def dibujar_matriz(m):
    for r in m:
        print(" | ".join(r))
        print("-" * 5)

def validar_ganador(m, pj):
    diagonales = [[(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]
    filas = [[(i, j) for j in range(3)] for i in range(3)]
    columnas = [[(j, i) for j in range(3)] for i in range(3)]
    for combo in diagonales + filas + columnas:
        if all(m[x][y] == pj for x, y in combo):
            return True
    return False

def turno(matriz, jugador):
    while True:
        f, c = map(int, input(f"{jugador}, elige fila y columna: ").split())
        if matriz[f][c] == " ":
            matriz[f][c] = jugador
            break
        else:
            print("Casilla ocupada, intenta de nuevo.")

def main():
    m = crear_matriz()
    j = "X"
    for paso in range(9):
        dibujar_matriz(m)
        turno(m, j)
        if validar_ganador(m, j):
            dibujar_matriz(m)
            print(f"¡Victoria de {j}!")
            return
        j = "O" if j == "X" else "X"
    dibujar_matriz(m)
    print("¡Empate!")

main()

