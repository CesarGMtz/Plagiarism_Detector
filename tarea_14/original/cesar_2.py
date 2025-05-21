def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    for turn in range(9):
        print_board(board)
        r, c = map(int, input(f"Jugador {player} (fila columna): ").split())
        if board[r][c] != " ":
            print("¡Ocupado!")
            continue
        board[r][c] = player
        if check_win(board, player):
            print_board(board)
            print(f"¡Jugador {player} gana!")
            return
        player = "O" if player == "X" else "X"
    print_board(board)
    print("¡Empate!")

tic_tac_toe()

