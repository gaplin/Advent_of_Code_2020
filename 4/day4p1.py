input = open('input2.txt').read().splitlines()

passports = []
current_passport = {}
for line in input:
    if line == '':
        passports.append(current_passport)
        current_passport = {}
        continue
    entries = line.split(' ')
    for entry in entries:
        key, value = entry.split(':')
        current_passport[key] = value
passports.append(current_passport)

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passwords = 0
for passport in passports:
    for required_key in required_keys:
        if required_key not in passport:
            break
    else:
        valid_passwords += 1

print(valid_passwords)