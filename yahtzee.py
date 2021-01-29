from random import randint

no_of_simulations = 100


def count_no_of_rolls():
    no_of_rolls = 0

    rolls = []

    ideal_rolls = []

    for i in range(1, 7):
        ideal_rolls.append([i]*5)

    while rolls not in ideal_rolls:
        no_of_rolls += 1
        rolls = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]

    return no_of_rolls


tallies = []
total = 0
for i in range(no_of_simulations):
    count = count_no_of_rolls()
    total += count
    tallies.append(count)

average = total/no_of_simulations

print(average)
