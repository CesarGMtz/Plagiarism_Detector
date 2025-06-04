tab = [[" "]*3 for _ in range(3)]
turno, fin = "X", False

mostrar = lambda: [print(" | ".join(row) + ("\n-----" if i < 2 else "")) for i, row in enumerate(tab)]

jugada_valida = lambda r, c: 0 <= r < 3 and 0 <= c < 3 and tab[r][c] == " "

def hay_triunfo(s):
    return any(all(tab[i][j] == s for j in range(3)) for i in range(3)) or \
           any(all(tab[j][i] == s for j in range(3)) for i in range(3)) or \
           all(tab[i][i] == s for i in range(3)) or all(tab[i][2 - i] == s for i in range(3))

for _ in range(9):
    mostrar()
    try:
        x, y = map(int, input(f"{turno} elige posición: ").split())
        if not jugada_valida(x, y):
            print("Ocupado o fuera de rango.")
            continue
        tab[x][y] = turno
        if hay_triunfo(turno):
            mostrar()
            print(f"{turno} ha ganado")
            fin = True
            break
        turno = "O" if turno == "X" else "X"
    except:
        print("Entrada no válida.")

if not fin:
    mostrar()
    print("Juego empatado")

