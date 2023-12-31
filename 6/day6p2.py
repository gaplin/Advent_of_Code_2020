from string import ascii_lowercase as asc_l

input = open('input2.txt').read().splitlines()

groups = []
current_group = set(asc_l)
for line in input:
    if line == '':
        groups.append(current_group)
        current_group = set(asc_l)
        continue
    current_group = current_group.intersection(line)
else:
    groups.append(current_group)

result = sum(map(len, groups))
print(result)