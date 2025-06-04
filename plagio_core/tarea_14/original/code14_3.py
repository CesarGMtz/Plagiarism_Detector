board = [[" " for _ in range(3)] for _ in range(3)]

def draw():
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(sym):
    for i in range(3):
        if board[i] == [sym]*3 or [board[j][i] for j in range(3)] == [sym]*3:
            return True
    return board[0][0] == sym == board[1][1] == board[2][2] or \
           board[0][2] == sym == board[1][1] == board[2][0]

turns = 0
player = "X"

while turns < 9:
    draw()
    row, col = map(int, input(f"{player} ingresa fila y columna: ").split())
    if board[row][col] != " ":
        print("Intento inválido")
        continue
    board[row][col] = player
    if is_winner(player):
        draw()
        print(f"¡{player} ha ganado!")
        break
    player = "O" if player == "X" else "X"
    turns += 1
else:
    draw()
    print("Empate")

