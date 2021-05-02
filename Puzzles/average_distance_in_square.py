from random import random

NO_OF_PAIRS = 10**6

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


total_distance = 0
for i in range(NO_OF_PAIRS):
    p1 = (random(), random())
    p2 = (random(), random())
    total_distance += distance(p1, p2)

average = total_distance/NO_OF_PAIRS
print(average)
