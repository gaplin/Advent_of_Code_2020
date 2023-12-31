input = open('input2.txt').read().splitlines()

valid_passwords = 0
for line in input: 
    occurs, char, password = line.split(' ')
    occurs_ints = list(map(int, occurs.split('-')))
    char = char[0]
    char_count = password.count(char)
    if occurs_ints[0] <= char_count <= occurs_ints[1]:
        valid_passwords += 1

print(valid_passwords)