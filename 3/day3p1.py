grid = open('input.txt').read().splitlines()
n = len(grid)
m = len(grid[0])
direction = (1, 3)

position = (0, 0)

trees = 0
while position[0] < n:
    i, j = position
    if grid[i][j] == '#':
        trees += 1
    di, dii = direction
    i += di
    j = (j + dii) % m
    position = (i, j)

print(trees)