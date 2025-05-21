def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(t):
    for fila in t:
        print(" | ".join(fila))
        print("-" * 5)

def verificar(tab, s):
    return any(
        all(tab[i][j] == s for j in range(3)) or
        all(tab[j][i] == s for j in range(3))
        for i in range(3)
    ) or all(tab[i][i] == s for i in range(3)) or all(tab[i][2 - i] == s for i in range(3))

def pedir_movimiento(simbolo):
    try:
        f = int(input(f"{simbolo} - Fila (0-2): "))
        c = int(input(f"{simbolo} - Col (0-2): "))
        return f, c
    except:
        return -1, -1

def ejecutar():
    t = crear_tablero()
    turno = 0
    simbolos = ["X", "O"]

    while True:
        imprimir_tablero(t)
        s = simbolos[turno % 2]
        f, c = pedir_movimiento(s)
        if 0 <= f < 3 and 0 <= c < 3 and t[f][c] == " ":
            t[f][c] = s
            if verificar(t, s):
                imprimir_tablero(t)
                print(f"Gana {s}")
                break
            elif all(t[i][j] != " " for i in range(3) for j in range(3)):
                imprimir_tablero(t)
                print("Empate")
                break
            turno += 1
        else:
            print("Movimiento no válido")

ejecutar()

