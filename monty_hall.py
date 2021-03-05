from random import randint, shuffle
from copy import deepcopy

no_of_simulations = 10**5

no_of_doors = 10
doors = [0 for i in range(no_of_doors-1)]
doors.append(1)

shuffle(doors)
car_door = doors.index(1)

print(doors)

goat_doors = [door for door in range(no_of_doors) if doors[door] == 0]
no_chosen = randint(0, no_of_doors-1)

print("no chosen :", no_chosen)
print("goat doors :", goat_doors)

temp = deepcopy(goat_doors)

win = False

for door in temp:
    if door != no_chosen:
        goat_doors.remove(door)
        print("goat shown:", door)
        break

print(goat_doors)

print(no_chosen)
