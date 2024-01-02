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

def get_key(player1, player2):
    return (tuple(player1), tuple(player2))


def play(player1: deque, player2: deque):
    already_played_games = set()
    while True:
        key = get_key(player1, player2)
        if key in already_played_games:
            return (1, player1)
        already_played_games.add(key)

        if len(player1) == 0:
            return (2, player2)
        elif len(player2) == 0:
            return(1, player1)
        
        winner = 1
        card1, card2 = player1.popleft(), player2.popleft()
        if len(player1) >= card1 and len(player2) >= card2:
            new_p1 = deque()
            new_p2 = deque()
            for i in range(card1):
                new_p1.append(player1[i])
            for i in range(card2):
                new_p2.append(player2[i])
            winner, _ =  play(new_p1, new_p2)
        else:
            if card1 > card2:
                winner = 1
            else:
                winner = 2
        if winner == 1:
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

_, winning_set = play(*players)

result = get_score(winning_set)
print(result)
