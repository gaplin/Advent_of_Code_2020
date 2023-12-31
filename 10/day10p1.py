jolts = list(map(int, open('input2.txt').read().splitlines()))

jolts.insert(0, 0)
jolts.sort()
jolts.append(jolts[len(jolts) - 1] + 3)
ones = 0
threes = 0
n = len(jolts)
for i in range(1, n):
    diff = jolts[i] - jolts[i - 1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1

print(ones * threes)