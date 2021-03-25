from random import randint


class Player:
    def __init__(self):
        self.throw = randint(1, 3)


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


NO_OF_GAMES = 10**6

results = {
    "Player 1": 0,
    "Player 2": 0,
    "Draw": 0
}

for game in range(NO_OF_GAMES):
    result = play_game()
    if result == 1:
        results["Player 1"] += 1
    elif result == -1:
        results["Player 2"] += 1
    else:
        results["Draw"] += 1

proportions = {
    "Player 1": results["Player 1"] / NO_OF_GAMES,
    "Draw": results["Draw"] / NO_OF_GAMES,
    "Player 2": results["Player 2"] / NO_OF_GAMES
}
print(results)
print(proportions)
