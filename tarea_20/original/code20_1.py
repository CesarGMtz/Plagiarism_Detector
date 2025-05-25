import random

def create_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    stack = [(1, 1)]
    maze[1][1] = ' '

    while stack:
        x, y = stack[-1]
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        moved = False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[y + dy//2][x + dx//2] = ' '
                stack.append((nx, ny))
                moved = True
                break
        if not moved:
            stack.pop()
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

maze = create_maze(21, 11)
print_maze(maze)

