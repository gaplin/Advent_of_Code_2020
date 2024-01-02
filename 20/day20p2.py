import math
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

top_left = []
for idx, node in enumerate(G):
    if node[(-1, 0)] == [] and node[(0, -1)] == []:
        top_left = idx
        break

n = math.isqrt(len(tiles))
image = [[-1 for _ in range(n)] for _ in range(n)]
image[0][0] = top_left

current_node = top_left
used_nodes = {tiles_with_rotations[top_left][0]}

for i in range(1, n):
    right_tiles = G[current_node][(0, 1)]
    assert len(right_tiles) == 1
    right_tile = right_tiles[0]
    tile_id = tiles_with_rotations[right_tile][0]
    assert tile_id not in used_nodes

    image[0][i] = right_tile
    used_nodes.add(tile_id)
    current_node = right_tile

for i in range(n):
    current_node = image[0][i]
    for ii in range(1, n):
        bot_tiles = G[current_node][(1, 0)]
        assert len(bot_tiles) == 1
        bot_tile = bot_tiles[0]
        tile_id = tiles_with_rotations[bot_tile][0]
        assert tile_id not in used_nodes

        image[ii][i] = bot_tile
        used_nodes.add(tile_id)
        current_node = bot_tile

tile_size = len(tiles[0][1])
new_tile_size = tile_size - 2
new_n = n * new_tile_size
expanded_image = [['.' for _ in range(new_n)] for _ in range(new_n)]

for i in range(n):
    for ii in range(n):
        tile = tiles_with_rotations[image[i][ii]][1]
        for iii in range(1, tile_size - 1):
            for iiii in range(1, tile_size - 1):
                expanded_image[new_tile_size * i + iii - 1][new_tile_size * ii + iiii - 1] = tile[iii][iiii]

all_rotations = get_all_rotations(expanded_image)


def get_possible_positions(i, ii):
    return [
        (i - 1, ii + 18),
        (i, ii), (i, ii + 5), (i, ii + 6), (i, ii + 11), (i, ii + 12), (i, ii + 17), (i, ii + 18), (i, ii + 19),
        (i + 1, ii + 1), (i + 1, ii + 4), (i + 1, ii + 7), (i + 1, ii + 10), (i + 1, ii + 13), (i + 1, ii + 16)
    ]

def get_matches(grid: list, n: int) -> int:
    result = 0
    markings = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n - 1):
        for ii in range(0, n - 19):
            possiible_position = get_possible_positions(i, ii)
            for y, x in possiible_position:
                if grid[y][x] != '#':
                    break
            else:
                for y, x in possiible_position:
                    markings[y][x] = 1
    
    for i in range(n):
        for ii in range(n):
            if grid[i][ii] == '#' and markings[i][ii] == 0:
                result += 1

    return result
    
result = new_n ** 2
for rotation in all_rotations:
    result = min(result, get_matches(rotation, new_n))

print(result)