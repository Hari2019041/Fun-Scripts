from random import randint


def isDuplicate(arr):
    temp = []
    for i in arr:
        if i in temp:
            return True
        else:
            temp.append(i)
    return False


YEAR = 365
NO_OF_PEOPLE = 70
NO_OF_SIMULATIONS = 10**5
successes = 0


for simulation in range(NO_OF_SIMULATIONS):
    birthdays = [randint(1, YEAR) for birthday in range(NO_OF_PEOPLE)]

    if isDuplicate(birthdays):
        successes += 1

probability = successes/NO_OF_SIMULATIONS
print(probability)
