N = 10**3

SQUARES = [int(i * i) for i in range(N+1)]


def is_possible(n):
    if n in SQUARES:
        return f"{n}"

    for square in SQUARES:
        if n - square in SQUARES:
            return f"{square} + {n-square}"

    return ""


impossible_squares = []
possible_squares = {}

for i in range(1, N + 1):
    if is_possible(i) == "":
        impossible_squares.append(i)
    else:
        possible_squares[i] = is_possible(i)

print(impossible_squares)
print(possible_squares)
