from random import shuffle, randint
from copy import deepcopy

no_of_prisoners = 100
no_of_boxes_opened = 100

prisoners = [False for i in range(no_of_prisoners)]


boxes = [i for i in range(no_of_prisoners)]
shuffle(boxes)

for prisoner in range(no_of_prisoners):
	box_no = 0
	
	temp = deepcopy(boxes)

	print(prisoner, end = ":")

	box_chosen = temp[randint]
	while box_no < no_of_boxes_opened and box_chosen != prisoner:
		print(box_chosen, end = " ")
		box_chosen = randint(0, 99)
		box_no += 1

	print(box_chosen)

	if box_chosen == prisoner:
		prisoners[prisoner] = True

print(prisoners)

