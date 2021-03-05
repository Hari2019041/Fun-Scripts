"""
    There exists a pond with certain no of lily pads in it and a frog before it
    and it wishes to get to the last lily pad.
    It can only move forward. At any given pad, it can hop to any of the
    forward pads with equal probability.
    This is a simulation to find out the average number of hops the frog will
    take to reach the last lily pad.
"""

from random import randint

NO_OF_SIMULATIONS = 10**6
SIZE_OF_POND = 10
no_of_steps_list = []


def simulation(SIZE_OF_POND):
    steps = 0
    pos = 0

    while (pos != SIZE_OF_POND):
        jump = randint(1, SIZE_OF_POND-pos)
        pos += jump
        steps += 1

    no_of_steps_list.append(steps)


for i in range(NO_OF_SIMULATIONS):
    simulation(SIZE_OF_POND)

average = sum(no_of_steps_list)/NO_OF_SIMULATIONS
print(average)
