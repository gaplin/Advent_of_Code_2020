input = map(int, open('input2.txt').read().splitlines())

target = 2020
present_nums = set()
result = 0
for num in input:
    remainder = target - num
    if remainder in present_nums:
        result = remainder * num
        break
    present_nums.add(num)

print(result)