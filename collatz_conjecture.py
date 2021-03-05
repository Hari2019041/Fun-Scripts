"""
    This is a fun testing of the famous unsolved Collatz Conjecture.
    The rules are as follows:
        If n is odd: n -> 3n+1
        If n is even: n -> n/2
    The Collatz Conjecture states that every number will eventually go to 1
    after a certain number of steps.
    This is to test and find the steps for the numbers.
"""

N = 10**5

list_of_steps = []
paths = ['']*N
paths[0] = '1'


def find_path(i):
    steps = 0
    no = i

    while no != 1:
        if no < i:
            paths[i-1] += paths[int(no)-1]
            steps += list_of_steps[int(no)-1]
            break

        paths[i-1] += str(int(no)) + '->'

        if no % 2 == 0:
            no = no/2
            steps += 1
        else:
            no = (3*no+1)/2
            steps += 2

    if paths[i-1][-1] != '1':
        paths[i-1] += '1'

    list_of_steps.append(steps)


for i in range(1, N+1):
    find_path(i)
    print(paths[i-1])
