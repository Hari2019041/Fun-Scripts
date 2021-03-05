from random import randint, shuffle

NO_OF_SIMULATIONS = 1000
NO_OF_PRISONERS = NO_OF_BOXES = 100

boxes = [i for i in range(NO_OF_BOXES)]

successes = 0
for simulation in range(NO_OF_SIMULATIONS):
    prisoners = [False for i in range(NO_OF_PRISONERS)]
    shuffle(boxes)

    for prisoner in range(NO_OF_PRISONERS):
        counter = 0
        box_searched = prisoner
        while counter < NO_OF_BOXES//2 and boxes[box_searched] != prisoner:
            box_searched = boxes[box_searched]
            counter += 1

        if boxes[box_searched] == prisoner:
            prisoners[prisoner] = True

    if prisoners == [True]*NO_OF_PRISONERS:
        successes += 1

success_rate = successes/NO_OF_SIMULATIONS

print(success_rate)
