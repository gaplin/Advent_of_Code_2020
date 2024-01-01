def to_onp(expression: str):
    result = []
    operands = []
    priorities = {'+': 0, '*': 0, '(': 2, ')': 1}
    for symbol in expression:
        if symbol == ' ':
            continue
        if symbol.isdigit():
            result.append(int(symbol))
        elif symbol in '+*':
            prio = priorities[symbol]
            while operands != [] and priorities[operands[-1]] <= prio:
                result.append(operands.pop())
            operands.append(symbol)
        elif symbol == ')':
            while operands[-1] != '(':
                result.append(operands.pop())
            operands.pop()
        elif symbol == '(':
            operands.append(symbol)

    while operands != []:
        result.append(operands.pop())
    
    return result

def eval_onp(onp: list):
    results = []
    for symbol in onp:
        if symbol == '+':
            b, a = results.pop(), results.pop()
            results.append(a + b)
        elif symbol == '*':
            b, a = results.pop(), results.pop()
            results.append(a * b)
        else:
            results.append(symbol)
    return results[0]

input = open('input2.txt').read().splitlines()

result = 0
for line in input:
    onp = to_onp(line)
    result += eval_onp(onp)

print(result)