import re

input = open('input2.txt').read().splitlines()

def apply_mask(mask, value):
    result = ''
    for x, y in zip(mask, value):
        if x == 'X':
            result += y
        else:
            result += x

    return result


mask = ''
mem = {}
for line in input:
    if line.startswith('mask = '):
        mask = line.split(' = ')[1]
        continue
    idx, num = [int(x) for x in re.findall('[0-9]+', line)]
    binary_num = '{0:036b}'.format(num)
    val = apply_mask(mask, binary_num)
    mem[idx] = int(val, 2)

result = sum(mem.values())
print(result)