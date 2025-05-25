import random

def create_maze(width, height):
    maze = [[' ' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if x % 2 == 0 or y % 2 == 0:
                maze[y][x] = '#'

    for y in range(1, height, 2):
        for x in range(1, width, 2):
            direction = random.choice([(0, -1), (1, 0)])
            dx, dy = direction
            if 0 <= x + dx < width and 0 <= y + dy < height:
                maze[y + dy][x + dx] = ' '

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

maze = create_maze(21, 11)
print_maze(maze)

