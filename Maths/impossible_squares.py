N = 10**3

SQUARES = {int(i * i) for i in range(N + 1)}


def find_possible(n):
    if n in SQUARES:
        return f'{n}'

    for square in SQUARES:
        if n - square in SQUARES:
            return f'{square} + {n-square}'

    return ''


impossible_squares = []
possible_squares = {}

for i in range(1, N + 1):
    temp = find_possible(i)
    if temp == '':
        impossible_squares.append(i)
    else:
        possible_squares[i] = temp

print(impossible_squares)
print(possible_squares)
