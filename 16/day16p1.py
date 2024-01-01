m = 1100

occurs = [0 for _ in range(m)]

input = open('input2.txt').read().splitlines()
n = len(input)
idx = 0
while True:
    line = input[idx]
    idx += 1
    if line == '':
        break
    ranges = line.split(': ')[1].split(' or ')
    for r in ranges:
        r = [int(x) for x in r.split('-')]
        occurs[r[0]] += 1
        occurs[r[1] + 1] += -1

for i in range(1, m):
    occurs[i] += occurs[i - 1]

idx += 4
result = 0
while idx < n:
    values = [int(x) for x in input[idx].split(',')]
    idx += 1
    for value in values:
        if occurs[value] == 0:
            result += value
print(result)