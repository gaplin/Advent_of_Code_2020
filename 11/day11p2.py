from functools import reduce

grid = list(map(lambda x: [y for y in x], open('input2.txt').read().splitlines()))

n = len(grid)
m = len(grid[0])

def adjacent_occupied_seats(grid, directions, n, m, i, ii):
    result = 0
    for di, dii in directions:
        step = 0
        while True:
            step += 1
            new_i, new_ii = i + di * step, ii + dii * step
            if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= m:
                break
            if grid[new_i][new_ii] == '#':
                result += 1
                break
            elif grid[new_i][new_ii] == 'L':
                break

    return result

def iterate(grid, n, m, directions):
    change_to_empty = []
    change_to_occupied = []

    for i in range(n):
        for ii in range(m):
            if grid[i][ii] != '.':
                occupied = adjacent_occupied_seats(grid, directions, n, m, i, ii)
                if grid[i][ii] == '#' and occupied >= 5:
                    change_to_empty.append((i, ii))
                elif grid[i][ii] == 'L' and occupied == 0:
                    change_to_occupied.append((i, ii))

    changed_places = len(change_to_empty) + len(change_to_occupied)
    for i, ii in change_to_empty:
        grid[i][ii] = 'L'
    for i, ii in change_to_occupied:
        grid[i][ii] = '#'

    return changed_places

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while True:
    changed_places = iterate(grid, n, m, directions)
    if changed_places == 0:
        break

result = reduce(lambda acc, x: acc + x.count('#'), grid, 0)
print(result)