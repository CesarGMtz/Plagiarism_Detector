def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print("\nEstado actual:")
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def movimiento_valido(tablero, fila, col):
    return 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == " "

def verificar_ganador(tablero, simbolo):
    for fila in tablero:
        if all(c == simbolo for c in fila):
            return True
    for col in range(3):
        if all(tablero[f][col] == simbolo for f in range(3)):
            return True
    if all(tablero[i][i] == simbolo for i in range(3)) or all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def jugar():
    tablero = inicializar_tablero()
    simbolos = ["X", "O"]
    turno = 0

    while True:
        mostrar_tablero(tablero)
        simbolo = simbolos[turno % 2]
        print(f"Turno de {simbolo}")
        try:
            fila = int(input("Fila (0-2): "))
            col = int(input("Columna (0-2): "))
        except:
            print("Entrada inválida.")
            continue
        if not movimiento_valido(tablero, fila, col):
            print("Movimiento no válido.")
            continue
        tablero[fila][col] = simbolo
        if verificar_ganador(tablero, simbolo):
            mostrar_tablero(tablero)
            print(f"¡{simbolo} gana!")
            break
        if all(c != " " for fila in tablero for c in fila):
            mostrar_tablero(tablero)
            print("Empate.")
            break
        turno += 1

jugar()

