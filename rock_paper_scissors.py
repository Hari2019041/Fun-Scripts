import random


class Player:
    def __init__(self):
        self.throw = random.randint(1, 3)


def play_game():
    player1 = Player()
    player2 = Player()

    throw1 = player1.throw
    throw2 = player2.throw

    if throw1 == throw2:
        return 0
    if throw1 == 1:
        return 1 if throw2 == 2 else -1
    elif throw1 == 2:
        return -1 if throw2 == 1 else 1
    return -1 if throw2 == 1 else 1


no_of_games = 10**6

results = {
    "Player 1": 0,
    "Player 2": 0,
    "Draw": 0
}

for game in range(no_of_games):
    result = play_game()
    if result == 1:
        results["Player 1"] += 1
    elif result == -1:
        results["Player 2"] += 1
    else:
        results["Draw"] += 1

proportions = {
    "Player 1": results["Player 1"]/no_of_games,
    "Draw": results["Draw"]/no_of_games,
    "Player 2": results["Player 2"]/no_of_games
}
print(results)
print(proportions)
