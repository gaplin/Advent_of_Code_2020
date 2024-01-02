input = open('input2.txt').read().splitlines()

tiles = []
current_tile = [0, []]
for line in input:
    if line == '':
        tiles.append(current_tile)
        current_tile = [0, []]
    elif line.startswith('Tile'):
        id = int(line[5:-1])
        current_tile[0] = id
    else:
        current_tile[1].append([x for x in line])
else:
    tiles.append(current_tile)

def tile_to_edges(tile: list) -> tuple:
    n = len(tile)
    top = int(''.join(tile[0]).replace('#', '1').replace('.', '0'), 2)
    bot = int(''.join(tile[n - 1]).replace('#', '1').replace('.', '0'), 2)
    left = ''
    right = ''
    for i in range(n):
        left += tile[i][0]
        right += tile[i][n - 1]
    left = int(left.replace('#', '1').replace('.', '0'), 2)
    right = int(right.replace('#', '1').replace('.', '0'), 2)

    return (top, right, bot, left)

def right_rotation(grid: list) -> list:
    n = len(grid)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for ii in range(n):
            result[i][ii] = grid[n - ii - 1][i]
    return result

def flip(grid: list) -> list:
    n = len(grid)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for ii in range(n):
            result[i][ii] = grid[n - i - 1][ii]

    return result

def get_all_rotations(grid: list) ->list:
    result = []
    current_rotation = grid
    for _ in range(4):
        result.append(current_rotation)
        current_rotation = right_rotation(current_rotation)

    current_rotation = flip(current_rotation)
    for _ in range(4):
        result.append(current_rotation)
        current_rotation = right_rotation(current_rotation)

    return result

def add_value_to_dict(d: dict, key, value):
    if key not in d:
        d[key] = []
    
    d[key].append(value)

tops = {}
lefts = {}
rights = {}
bots = {}

tiles_with_rotations = []
for id, tile in tiles:
    rotations = get_all_rotations(tile)
    for rotation in rotations:
        edges = tile_to_edges(rotation)
        t, r, b, l = edges
        tiles_with_rotations.append((id, rotation, edges))
        idx = len(tiles_with_rotations) - 1
        add_value_to_dict(tops, t, idx)
        add_value_to_dict(rights, r, idx)
        add_value_to_dict(bots, b, idx)
        add_value_to_dict(lefts, l, idx)

N = len(tiles_with_rotations)
G = [
    {
        (0, 1): [],
        (0, -1): [],
        (1, 0): [],
        (-1, 0): []
    }
    for _ in range(N)
    ]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for idx, value in enumerate(tiles_with_rotations):
    tile_id = value[0]
    t, r, b, l = value[2]
    for id in bots[t]:
        if id != idx and tile_id != tiles_with_rotations[id][0]:
            G[idx][(-1, 0)].append(id)

    for id in lefts[r]:
        if id != idx and tile_id != tiles_with_rotations[id][0]:
            G[idx][(0, 1)].append(id)
    
    for id in tops[b]:
        if id != idx and tile_id != tiles_with_rotations[id][0]:
            G[idx][(1, 0)].append(id)
    
    for id in rights[l]:
        if id != idx and tile_id != tiles_with_rotations[id][0]:
            G[idx][(0, -1)].append(id)

top_lefts = set()
for idx, node in enumerate(G):
    if node[(1, 0)] == [] and node[(0, -1)] == []:
        top_lefts.add(tiles_with_rotations[idx][0])

assert len(top_lefts) == 4

result = 1
for value in top_lefts:
    result *= value
print(result)
