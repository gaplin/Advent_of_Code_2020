from collections import deque

input = open('input2.txt').read().splitlines()

players = []
current_player = deque()
for line in input:
    if line == '':
        players.append(current_player)
        current_player = deque()
        continue
    if line.startswith('P'):
        continue
    current_player.append(int(line))
else:
    players.append(current_player)


def make_a_turn(player1: deque, player2: deque):
    card1, card2 = player1.popleft(), player2.popleft()
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)

def get_score(player: deque):
    mult = 1
    result = 0
    while len(player) > 0:
        result += mult * player.pop()
        mult += 1

    return result

result = 0
while True:
    finish = False
    for idx, player in enumerate(players):
        if len(player) == 0:
            finish = True
            result = get_score(players[1 - idx])
            break
    if finish == True:
        break
    make_a_turn(*players)

print(result)