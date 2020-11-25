N = 10**4

list_of_steps = []
paths = [""]*N
paths[0] = "1"

def finding_path(i):
	steps = 0
	no = i

	while no != 1:
		if no < i:
			paths[i-1] += paths[int(no)-1]
			steps += list_of_steps[int(no)-1]	
			break

		paths[i-1] += str(int(no)) + "->"

		if no%2 == 0:
			no = no/2
			steps += 1
		else:
			no = (3*no+1)/2
			steps += 2

	if paths[i-1][-1] != "1":
		paths[i-1] += "1"

	list_of_steps.append(steps)

for i in range(1, N+1):
	finding_path(i)
	print(paths[i-1])


