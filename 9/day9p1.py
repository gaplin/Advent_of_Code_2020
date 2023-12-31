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

result = 0
for i in range(preamble, n):
    num = numbers[i]
    if exist_value(num, pairs) == False:
        result = num
        break
    for j in range(1, preamble):
        add_value(num + numbers[i - j], pairs)
        remove_value(numbers[i - preamble] + numbers[i - preamble + j], pairs)

print(result)