input = open('input2.txt').read().splitlines()

def move(position: list, direction: str) -> None:
    steps_map = {
        'w': (-2, 0),
        'e': (2, 0),
        'ne': (1, 1),
        'nw': (-1, 1),
        'se': (1, -1),
        'sw': (-1, -1)
    }
    dx, dy = steps_map[direction]
    position[0] += dx
    position[1] += dy

tiles = {}
for line in input:
    n = len(line)
    i = 0
    current_position = [0, 0]
    while i < n:
        direction = ''
        if line[i] in 'sn':
            direction = line[i] + line[i + 1]
            i += 1
        else:
            direction = line[i]
        move(current_position, direction)
        i += 1
    position_tuple = tuple(current_position)
    if position_tuple not in tiles:
        tiles[position_tuple] = 0
    
    tiles[position_tuple] += 1

white_tiles = set()
black_tiles = set()
for position, value in tiles.items():
    if value % 2 == 1:
        black_tiles.add(position)
    else:
        white_tiles.add(position)


def execute_process(black_tiles: set(), directions: list):
    white_tiles_to_move = []
    black_tiles_to_move = []
    black_neighbours = {}

    for x, y in black_tiles:
        b_neighbours = 0
        for dx, dy in directions:
            neighbour = (x + dx, y + dy)
            if neighbour not in black_neighbours:
                    black_neighbours[neighbour] = 0
            black_neighbours[neighbour] += 1
            if neighbour in black_tiles:
                b_neighbours += 1
        if b_neighbours == 0 or b_neighbours > 2:
            black_tiles_to_move.append((x, y))
    
    for tile, b_count in black_neighbours.items():
        if tile not in black_tiles and b_count == 2:
            white_tiles_to_move.append(tile)

    for tile in black_tiles_to_move:
        black_tiles.remove(tile)

    for tile in white_tiles_to_move:
        black_tiles.add(tile)

directions = [(-2, 0), (2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for i in range(100):
    execute_process(black_tiles, directions)

print(len(black_tiles)) 