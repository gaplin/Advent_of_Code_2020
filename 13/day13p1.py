import re

input = open('input2.txt').read().splitlines()

stamp = int(input[0])
ids = list(map(int, re.findall('[0-9]+', input[1])))

def get_earliest_time(stamp, id):
    mod = stamp % id
    if mod == 0:
        return stamp
    return stamp + id - mod

result = 0
earliest_time = 9999999999999999999999

for id in ids:
    time_for_id = get_earliest_time(stamp, id)
    if time_for_id < earliest_time:
        result = id * (time_for_id - stamp)
        earliest_time = time_for_id

print(result)