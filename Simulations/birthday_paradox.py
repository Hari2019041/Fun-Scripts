from random import randint


def isDuplicate(arr):
    temp = set()
    for i in arr:
        if i in temp:
            return True
        else:
            temp.add(i)
    return False


YEAR = 365
NO_OF_PEOPLE = 70
NO_OF_SIMULATIONS = 10**5
successes = 0

for simulation in range(NO_OF_SIMULATIONS):
    birthdays = [randint(1, YEAR) for birthday in range(NO_OF_PEOPLE)]
    successes += 1 if isDuplicate(birthdays) else 0


probability = successes / NO_OF_SIMULATIONS
print(probability)
