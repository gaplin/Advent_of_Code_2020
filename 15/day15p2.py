nums = list(map(int, open('input2.txt').read().split(',')))

def make_a_turn(nums: list, history: dict, last_num: int) -> int:
    if len(nums) > 0:
        return nums.pop(0)
    
    if last_num not in history or len(history[last_num]) == 1:
        return 0
    
    return history[last_num][1] - history[last_num][0]

def update_history(history: dict, value: int, turn: int) -> None:
    if value not in history:
        history[value] = []

    history[value].append(turn)
    if len(history[value]) > 2 :
        history[value].pop(0)

result = 0
history = {}
for i in range(0, 30000000):
    result = make_a_turn(nums, history, result)
    update_history(history, result, i)
    
print(result)