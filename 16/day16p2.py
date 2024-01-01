m = 1100

occurs = [0 for _ in range(m)]

input = open('input2.txt').read().splitlines()
n = len(input)
idx = 0
entries = {}
while True:
    line = input[idx]
    idx += 1
    if line == '':
        break
    key, ranges = line.split(': ')
    ranges = ranges.split(' or ')
    dict_value = []
    for r in ranges:
        r = [int(x) for x in r.split('-')]
        dict_value.append(r)
        occurs[r[0]] += 1
        occurs[r[1] + 1] += -1
    entries[key] = dict_value

for i in range(1, m):
    occurs[i] += occurs[i - 1]

idx += 1
my_ticket = [int(x) for x in input[idx].split(',')]

idx += 3
result = 0
valid_tickets = []
while idx < n:
    values = [int(x) for x in input[idx].split(',')]
    idx += 1
    for value in values:
        if occurs[value] == 0:
            break
    else:
        valid_tickets.append(values)


def get_valid_arrangement(current_arrangement: tuple, entries: dict, valid_tickets: list, idx, m: int, not_available_keys: tuple, cache: dict) -> tuple:
    cache_key = not_available_keys
    if cache_key in cache:
        return cache[cache_key]
    if idx >= m:
        cache[cache_key] = current_arrangement
        return current_arrangement

    valid_keys = []
    for key, ranges in entries.items():
        if key in not_available_keys:
            continue
        valid_key = False
        for ticket in valid_tickets:
            ticket_value = ticket[idx]
            valid_ticket = False
            for low, high in ranges:
                if low <= ticket_value <= high:
                    valid_ticket = True
                    break
            if valid_ticket == False:
                break
        else:
            valid_key = True
        if valid_key == True:
            valid_keys.append(key)
    
    result = ()
    for key in valid_keys:
        arrangement = (*current_arrangement, key)
        not_available_keys = tuple(sorted(arrangement))
        key_result = get_valid_arrangement(arrangement, entries, valid_tickets, idx + 1, m, not_available_keys, cache)
        if key_result != ():
            result = key_result
            break

    cache[cache_key] = result
    return result

arr = get_valid_arrangement((), entries, valid_tickets, 0, len(my_ticket), (), {})

result = 1
for key, value in zip(arr, my_ticket):
    if key.startswith('departure'):
        result *= value

print(result)