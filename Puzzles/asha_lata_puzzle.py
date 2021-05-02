squares = []
for i in range(32, 99):
    squares.append(i**2)

for i in squares:
    asha = i//100
    lata = i%100

    new_number = (asha+11)*100 + (lata+11)
    if new_number in squares:
        break

print(asha, lata)
