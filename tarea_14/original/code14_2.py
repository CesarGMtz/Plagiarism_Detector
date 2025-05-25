def display(grid):
    for line in grid:
        print(" | ".join(line))
        print("-" * 5)

def won(grid, p):
    return any(all(cell == p for cell in row) for row in grid) or \
           any(all(grid[i][j] == p for i in range(3)) for j in range(3)) or \
           all(grid[i][i] == p for i in range(3)) or \
           all(grid[i][2 - i] == p for i in range(3))

grid = [[" "] * 3 for _ in range(3)]
current = "X"
moves = 0

while moves < 9:
    display(grid)
    i, j = map(int, input(f"Turno de {current}: ").split())
    if grid[i][j] != " ":
        print("Casilla ocupada")
        continue
    grid[i][j] = current
    moves += 1
    if won(grid, current):
        display(grid)
        print(f"{current} gana!")
        break
    current = "O" if current == "X" else "X"
else:
    display(grid)
    print("Empate")

