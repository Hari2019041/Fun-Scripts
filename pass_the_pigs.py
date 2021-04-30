from random import randint

DEATH_ROLL = 1
NO_OF_SIMULATIONS = 10**3
TARGET_SCORE = 100

# A turn is made up of multiple rolls

# This finds out the number of TURNS it takes to reach 100
def roll_strategy_to_100(rolls=5):
    no_of_turns_taken = 0
    running_score = 0
    while running_score < TARGET_SCORE:
        no_of_rolls = 0
        no_of_turns_taken += 1
        current_score = 0
        while no_of_rolls < rolls:
            roll = randint(1, 6)
            no_of_rolls += 1
            if roll == DEATH_ROLL:
                current_score = 0
                break
            else:
                current_score += roll
        running_score += current_score
    return no_of_turns_taken


def score_strategy(score=20):
    pass


# Initializations
roll_strategies_to_100 = {}
for i in range(1, 21):
    roll_strategies_to_100[i] = 0

for simulation in range(NO_OF_SIMULATIONS):
    for i in range(1, 21):
        roll_strategies_to_100[i] += roll_strategy_to_100(i)

for i in range(1, 21):
    roll_strategies_to_100[i] /= NO_OF_SIMULATIONS

print(roll_strategies_to_100)
