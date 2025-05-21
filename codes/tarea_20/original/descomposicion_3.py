import random

def init_maze(width, height):
    return [['#' for _ in range(width)] for _ in range(height)]

def generate_maze(maze, start):
    stack = [start]
    width, height = len(maze[0]), len(maze)
    maze[start[1]][start[0]] = ' '

    while stack:
        x, y = stack[-1]
        dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(dirs)
        found = False
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[y + dy//2][x + dx//2] = ' '
                stack.append((nx, ny))
                found = True
                break
        if not found:
            stack.pop()

def print_maze(maze):
    for row in maze:
        print(''.join(row))

maze = init_maze(21, 11)
generate_maze(maze, (1, 1))
print_maze(maze)

