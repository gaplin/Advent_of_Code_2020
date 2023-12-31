input = open('input2.txt').read().splitlines()

moves = [x for x in map(lambda x: (x[0], int(x[1:])), input)]

directions = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

def turn_L(facing, times):
    assert 1 <= times <= 3
    for _ in range(times):
        facing[0], facing[1] = -facing[1], facing[0]

def turn_R(facing, times):
    assert 1 <= times <= 3
    for _ in range(times):
        facing[0], facing[1] = facing[1], -facing[0]

position = [0, 0]
waypoint = [10, 1]

for command, steps in moves:
    if command == 'F':
        position[0] += steps * waypoint[0]
        position[1] += steps * waypoint[1]
    elif command == 'L':
        turns = steps // 90
        turn_L(waypoint, turns)
    elif command == 'R':
        turns = steps // 90
        turn_R(waypoint, turns)
    else:
        dx, dy = directions[command]
        waypoint[0] += steps * dx
        waypoint[1] += steps * dy

result = abs(position[0]) + abs(position[1])
print(result)