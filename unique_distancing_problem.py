from random import sample

GRID_SIZE = 6

choices = [i for i in range(GRID_SIZE**2)]


def distance(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


for k in range(1000000):
    towns = sample(choices, GRID_SIZE)
    points = [(i // GRID_SIZE, i % GRID_SIZE) for i in towns]
    distances = set()
    isValid = True
    for i in range(GRID_SIZE):
        for j in range(i + 1, GRID_SIZE):
            temp = distance(points[i], points[j])**0.5
            isValid = False if temp in distances else True
            distances.add(temp)

    if isValid:
        print(points)
        break
