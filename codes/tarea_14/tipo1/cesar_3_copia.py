matriz = [[" " for _ in range(3)] for _ in range(3)]

def dibujar():
    for linea in matriz:
        print(" | ".join(linea))
        print("-----")

def victoria(j):
    for i in range(3):
        if matriz[i] == [j]*3:
            return True
        if [matriz[x][i] for x in range(3)] == [j]*3:
            return True
    if matriz[0][0] == j and matriz[1][1] == j and matriz[2][2] == j:
        return True
    if matriz[0][2] == j and matriz[1][1] == j and matriz[2][0] == j:
        return True
    return False

jugador = "X"
turnos = 0

while turnos < 9:
    dibujar()
    f, c = map(int, input(f"Turno {jugador}: ").split())
    if matriz[f][c] != " ":
        print("Casilla no disponible")
        continue
    matriz[f][c] = jugador
    if victoria(jugador):
        dibujar()
        print(f"¡Ganó {jugador}!")
        break
    jugador = "O" if jugador == "X" else "X"
    turnos += 1
else:
    dibujar()
    print("Empate")

