input = open('input2.txt').read().splitlines()

rules = {}
messages = []
processing_rules = True
for line in input:
    if line == '':
        processing_rules = False
        continue
    if processing_rules:
        id, rule = line.split(': ')
        rules[id] = []
        rule_set = rule.split(' | ')
        for rule in rule_set:
            rule = rule.split(' ')
            rules[id].append(rule)
    else:
        messages.append(line)

def get_max_matching_fragment(current_rule: str, rules: dict, message: str):
    all_rules = rules[current_rule]
    if len(all_rules) == 1 and '"' in all_rules[0][0]:
        if message[0] == all_rules[0][0][1]:
            return message[0]
        return ''
    
    result = ''
    for rule_set in all_rules:
        satisfied_fragment = ''
        current_fragment = message
        rule_set_satisfied = True
        for rule in rule_set:
            if current_fragment == '':
                rule_set_satisfied = False
                break
            matching_fragment = get_max_matching_fragment(rule, rules, current_fragment)
            satisfied_fragment += matching_fragment
            if matching_fragment == '':
                rule_set_satisfied = False
                break
            current_fragment = current_fragment[len(matching_fragment):]

        if rule_set_satisfied == True and len(result) < len(satisfied_fragment):
            result = satisfied_fragment

    return result

matches = 0
for message in messages:
    matched_fragment = get_max_matching_fragment('0', rules, message)
    if message == matched_fragment:
        matches += 1

print(matches)

    