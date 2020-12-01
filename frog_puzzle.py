# There exists a pond with certain no of lily pads in it and a frog before it
# and it wishes to get to the last lily pad.
# It can only move forward. At any given pad, it can hop to the other pads with
# equal probability.
# This is a simulation to find out the average number of hops the frog will
# take to reach the last lily pad.

from random import randint

no_of_simulations = 10**6
size_of_pond = 100
no_of_steps_list = []


def simulation(size_of_pond):
    steps = 0
    pos = 0

    while (pos != size_of_pond):
        jump = randint(1, size_of_pond-pos)
        pos += jump
        steps += 1

    no_of_steps_list.append(steps)


for i in range(no_of_simulations):
    simulation(size_of_pond)

average = sum(no_of_steps_list)/no_of_simulations
print(average)
