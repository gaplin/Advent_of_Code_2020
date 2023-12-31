numbers = list(map(int, open('input2.txt').read().splitlines()))

def add_value(value: int, pairs: dict):
    if value not in pairs:
        pairs[value] = 0
    pairs[value] += 1

def remove_value(value: int, pairs: dict):
    pairs[value] -= 1
    if pairs[value] == 0:
        del pairs[value]

def exist_value(value: int, pairs: dict) -> bool:
    return value in pairs

n = len(numbers)
pairs = {}
preamble = 25
for i in range(1, preamble):
    for j in range(i):
        add_value(numbers[i] + numbers[j], pairs)

target = 0
for i in range(preamble, n):
    num = numbers[i]
    if exist_value(num, pairs) == False:
        target = num
        break
    for j in range(1, preamble):
        add_value(num + numbers[i - j], pairs)
        remove_value(numbers[i - preamble] + numbers[i - preamble + j], pairs)

prefix_sum = [numbers[0]]

for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + numbers[i])

result = 0
for i in range(0, n - 1):
    result_found = False
    for j in range(i + 1, n):
        range_sum = 0
        if i == 0:
            range_sum = prefix_sum[j]
        else:
            range_sum = prefix_sum[j] - prefix_sum[i - 1]
        if range_sum == target:
            range = numbers[i:j + 1]
            min_value = min(range)
            max_value = max(range)
            result = min_value + max_value
            result_found = True
            break
    if result_found == True:
        break   

print(result)