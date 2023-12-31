grid = open('input2.txt').read().splitlines()
n = len(grid)
m = len(grid[0])
directions = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

result = 1
for di, dii in directions:
    position = (0, 0)
    trees = 0
    while position[0] < n:
        i, j = position
        if grid[i][j] == '#':
            trees += 1
        i += di
        j = (j + dii) % m
        position = (i, j)
    result *= trees

print(result)