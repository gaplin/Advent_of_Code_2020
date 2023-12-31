input = open('input2.txt').read().splitlines()

operations = [(x, int(y)) for x, y in map(lambda x: x.split(' '), input)]

def execute(code: str, argument: int, status: list):
    if code == 'nop':
        status[1] += 1
    elif code == 'jmp':
        status[1] += argument
    elif code == 'acc':
        status[0] += argument
        status[1] += 1
    else:
        raise Exception('invalid code')
    
status = [0, 0] # [0] -> acc, [1] => ip
executed_instructions = set()
while True:
    operation = operations[status[1]]
    execute(operation[0], operation[1], status)
    if status[1] in executed_instructions:
        break
    executed_instructions.add(status[1])

print(status[0])