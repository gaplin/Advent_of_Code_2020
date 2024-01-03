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

result = 0
for value in tiles.values():
    if value % 2 == 1:
        result += 1 

print(result)