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

dp = [0 for _ in range(n)]
dp[n - 1] = 1
for i in reversed(range(0, n - 1)):
    possibilities = 0
    jolt = jolts[i]
    for j in range(i + 1, n):
        if jolts[j] - jolt > 3:
            break
        possibilities += dp[j]

    dp[i] = possibilities

print(dp[0])