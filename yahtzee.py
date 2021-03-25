from random import randint

NO_OF_SIMULATIONS = 100
NO_OF_DICE = 5


def count_no_of_rolls():
    no_of_rolls = 0

    ideal_rolls = [[i] * NO_OF_DICE for i in range(1, 7)]

    rolls = []
    while rolls not in ideal_rolls:
        no_of_rolls += 1
        rolls = [randint(1, 6) for i in range(NO_OF_DICE)]

    return no_of_rolls


total = 0
for simulation in range(NO_OF_SIMULATIONS):
    count = count_no_of_rolls()
    total += count

average = total / NO_OF_SIMULATIONS
print(average)
