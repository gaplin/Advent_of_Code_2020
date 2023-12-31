input = open('input2.txt').read().splitlines()

groups = []
current_group = set()
for line in input:
    if line == '':
        groups.append(current_group)
        current_group = set()
        continue
    for char in line:
        current_group.add(char)
else:
    groups.append(current_group)

result = sum(map(len, groups))
print(result)