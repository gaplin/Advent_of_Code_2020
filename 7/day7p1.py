import re

input = open('input2.txt').read().splitlines()

G = {}
for line in input:
    bags = re.findall('(?:[a-z]+ ){2}bag', line)
    first_bag = ''
    for idx, bag in enumerate(bags):
        if bag == 'no other bag':
            break
        bag = bag[:-4]
        if bag not in G:
            G[bag] = []
        if idx == 0:
            first_bag = bag
        else:
            G[bag].append(first_bag)

def dfs(G: dict, visited: set, v: str) -> int:
    visited.add(v)
    result = 1
    for u in G[v]:
        if u not in visited:
            result += dfs(G, visited, u)
    
    return result
        
result = dfs(G, set(), 'shiny gold') - 1

print(result)