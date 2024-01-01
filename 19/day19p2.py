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

def get_matching_fragments(current_rule: str, rules: dict, message: str) -> set:
    all_rules = rules[current_rule]
    if len(all_rules) == 1 and '"' in all_rules[0][0]:
        if message[0] == all_rules[0][0][1]:
            return {message[0]}
        return set()
    
    result = set()
    for rule_set in all_rules:
        satisfied_fragments = set()
        current_fragments = {message}
        num_of_rules = len(rule_set)
        for idx, rule in enumerate(rule_set):
            new_fragments = set()
            for word in current_fragments:
                matching_fragments = get_matching_fragments(rule, rules, word)
                if idx == num_of_rules - 1:
                    prefix = message[:-len(word)]
                    for fragment in matching_fragments:
                        satisfied_fragments.add(prefix + fragment)
                else:
                    for fragment in matching_fragments:
                        not_matched_fragment = word[len(fragment):]
                        if not_matched_fragment != '':
                            new_fragments.add(not_matched_fragment)
            current_fragments = new_fragments
            if len(current_fragments) == 0:
                break

        result |= satisfied_fragments

    return result

matches = 0
for message in messages:
    matched_fragments = get_matching_fragments('0', rules, message)
    if message in matched_fragments:
        matches += 1

print(matches)