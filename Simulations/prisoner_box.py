from random import shuffle

NO_OF_SIMULATIONS = 10**4
NO_OF_PRISONERS = NO_OF_BOXES = 100

boxes = [i for i in range(NO_OF_BOXES)]

successes = 0
for simulation in range(NO_OF_SIMULATIONS):
    prisoners = [False for i in range(NO_OF_PRISONERS)]
    shuffle(boxes)

    for prisoner in range(NO_OF_PRISONERS):
        counter = 0
        box_searched = prisoner
        while counter < NO_OF_BOXES // 2 and boxes[box_searched] != prisoner:
            box_searched = boxes[box_searched]
            counter += 1

        prisoners[prisoner] = True if boxes[box_searched] == prisoner else 0

    successes += 1 if prisoners == [True] * NO_OF_PRISONERS else 0


success_rate = successes / NO_OF_SIMULATIONS
print(success_rate)
