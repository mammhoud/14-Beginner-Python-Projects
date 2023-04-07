import random


def play():
    user = input('(r) for rock, (p) for paper, (s) for scissors\n')
    computer = str(random.choice(['r', 'p', 's']))

    if user == computer:
        return "its a tie"

    if is_win(user, computer):
        return "you won"

    return "you lost"
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') |(player == 'p' and opponent == 'r') |(player == 's' and opponent == 'p'):
        return True


while True:
    print(play())