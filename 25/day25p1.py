input = open('input2.txt').read().splitlines()

subject_number = 7
card_key = int(input[0])
door_key = int(input[1])
p = 20201227

def transform(subject_number, loop_size, p):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= p
    
    return value

loop_size = 1
value = 1
result = 0
while True:
    value *= subject_number
    value %= p
    if value == card_key:
        result = transform(door_key, loop_size, p)
        break
    if value == door_key:
        result = transform(card_key, loop_size, p)
        break
    loop_size += 1

print(result)