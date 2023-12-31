input = list(map(int, open('input2.txt').read().splitlines()))

target = 2020
result = 0
for i, num in enumerate(input):
    present_nums = set()
    new_target = target - num
    for num2 in input[i:]:
        remainder = new_target - num2
        if remainder in present_nums:
            result = remainder * num2 * num
            break
        present_nums.add(num2)
    if result > 0:
        break

print(result)