import re

input = open('input2.txt').read().splitlines()

def apply_mask(mask, value):
    results = ['']
    n = 1
    for x, y in zip(mask, value):
        if x == '0':
            for i in range(n):
                results[i] += y
        elif x == '1':
            for i in range(n):
                results[i] += '1'
        else:
            for i in range(n):
                results.append(results[i] + '1')
                results[i] += '0'
            n *= 2

    return results


mask = ''
mem = {}
for line in input:
    if line.startswith('mask = '):
        mask = line.split(' = ')[1]
        continue
    idx, num = [int(x) for x in re.findall('[0-9]+', line)]
    binary_num = '{0:036b}'.format(idx)
    values = apply_mask(mask, binary_num)
    for addr in values:
        mem[int(addr, 2)] = num

result = sum(mem.values())
print(result)