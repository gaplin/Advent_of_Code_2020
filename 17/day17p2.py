def get_directions(n: int) -> list:
    result = []
    nums = [0, 1, -1]
    limit = 3 ** n
    for i in range(1, limit):
        j = i
        direction = []
        for _ in range(n):
            mod = j % 3
            direction.append(nums[mod])
            j //= 3
        result.append(tuple(direction))

    return result

def cycle(active: set(), directions: list):
    affected = {}
    for x, y, z, w in active:
        for dx, dy, dz, dw in directions:
            cube = (x + dx, y + dy, z + dz, w + dw)
            if cube not in affected:
                affected[cube] = 0
            affected[cube] += 1
    
    new_actives = set()
    for cube, actives in affected.items():
        if cube in active:
            if 2 <= actives <= 3:
                new_actives.add(cube)
        else:
            if actives == 3:
                new_actives.add(cube)

    return new_actives

directions = get_directions(4)
input = open('input2.txt').read().splitlines()
n = len(input)
m = len(input[0])

active = set()
for i in range(n):
    for ii in range(m):
        if input[i][ii] == '#':
            active.add((ii, i, 0, 0))

for _ in range(6):
    active = cycle(active, directions)

print(len(active))