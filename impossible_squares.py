N = 10**2

squares = [int(i * i) for i in range(101)]


def is_possible(n):
    if n in squares:
        return f"{n}"

    for square in squares:
        if n - square in squares:
            return f"{square} + {n-square}"

    return ""


impossible_squares = []
possible_squares = {}

for i in range(1, N + 1):
    if is_possible(i) == "":
        impossible_squares.append(i)
    else:
        possible_squares[i] = is_possible(i)
