import re

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

def valid_byr(value: str) -> bool:
    if len(value) == 4 and len([x for x in value if x.isdigit()]) == 4:
        int_value = int(value)
        return 1920 <= int_value <= 2002
    return False

def valid_iyr(value: str) -> bool:
    if len(value) == 4 and len([x for x in value if x.isdigit()]) == 4:
        int_value = int(value)
        return 2010 <= int_value <= 2020
    return False

def valid_eyr(value: str) -> bool:
    if len(value) == 4 and len([x for x in value if x.isdigit()]) == 4:
        int_value = int(value)
        return 2020 <= int_value <= 2030
    return False

def valid_hgt(value: str) -> bool:
    limits = []
    if value.endswith('cm'):
        limits = [150, 193]
    elif value.endswith('in'):
        limits = [59, 76]
    if len(limits) == 2:
        heigth_str = value[:-2]
        if len(heigth_str) == len([x for x in heigth_str if x.isdigit()]):
            height_num = int(heigth_str)
            return limits[0] <= height_num <= limits[1]
        return False
    return False

def valid_hcl(value: str) -> bool:
    matches = re.findall('^#[0-9a-f]{6}', value)
    return len(matches) == 1 and matches[0] == value

def valid_ecl(value: str) -> bool:
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(value: str) -> bool:
    return len(value) == 9 and len([x for x in value if x.isdigit()]) == 9

required_keys = [('byr', valid_byr), ('iyr', valid_iyr), ('eyr', valid_eyr), ('hgt', valid_hgt), ('hcl', valid_hcl), ('ecl', valid_ecl), ('pid', valid_pid)]
valid_passwords = 0
for passport in passports:
    for required_key, validation in required_keys:
        if required_key not in passport or validation(passport[required_key]) == False:
            break
    else:
        valid_passwords += 1

print(valid_passwords)