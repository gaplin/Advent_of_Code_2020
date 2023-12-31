import re

input = open('input2.txt').read().splitlines()

G = {}
for line in input:
    bags = re.findall('(?:[0-9]+ )?(?:[a-z]+ ){2}bag', line)
    first_bag = ''
    for idx, bag in enumerate(bags):
        if bag == 'no other bag':
            break
        bag = bag[:-4]
        if idx == 0:
            if bag not in G:
                G[bag] = []
            first_bag = bag
            continue
        else:
            bag = bag.split(' ', 1)
            if bag[1] not in G:
                G[bag[1]] = []
            count = int(bag[0])
            G[first_bag].append((bag[1], count))

def dfs(G: dict, v: str) -> int:
    result = 1
    for u, count in G[v]:
        result += count * dfs(G, u)
    
    return result
        
result = dfs(G, 'shiny gold') - 1

print(result)