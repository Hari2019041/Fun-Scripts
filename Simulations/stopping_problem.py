from random import randint

NO_OF_TEST_CASES = 1000
NO_OF_TOILETS = 1000
QUALITY_RANGE = 10**10

STOPPING_POINT = int(0.37 * NO_OF_TOILETS)
successes = 0

for test_case in range(NO_OF_TEST_CASES):
    toilets = [randint(0, QUALITY_RANGE) for i in range(NO_OF_TOILETS)]
    best_toilet = max(toilets)
    best_toilet_yet = -1

    for i in range(NO_OF_TOILETS):
        if i <= STOPPING_POINT:
            if toilets[i] >= best_toilet_yet:
                best_toilet_yet = toilets[i]
        else:
            if toilets[i] > best_toilet_yet:
                best_toilet_yet = toilets[i]
                successes += 1 if best_toilet_yet == best_toilet else 0
                break

probability = successes / NO_OF_TEST_CASES

print(probability)
