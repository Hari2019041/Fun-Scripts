from random import shuffle, randint

NO_OF_SIMULATIONS = 10**6
NO_OF_DOORS = 3
GOAT = 0
CAR = 1

doors = [0]*(NO_OF_DOORS-1)
doors.append(1)

winning_car = 0
winning_goat = 0

def always_switch_strategy():
    shuffle(doors)

    car = doors.index(1)
    goats = [i for i in range(NO_OF_DOORS) if i != car]

    person_choice = randint(0, NO_OF_DOORS-1)

    doors_opened = [False for door in doors]
    if person_choice == car:
        for i in range(NO_OF_DOORS):
            doors_opened[i] = True if i in goats[:len(goats)-1] else False
        person_choice = [i for i in range(NO_OF_DOORS) if i != car and doors_opened[i] == False][0]
    else:
        for i in range(NO_OF_DOORS):
            doors_opened[i] = True if i != car and i != person_choice else False
        person_choice = [i for i in range(NO_OF_DOORS) if i != person_choice and doors_opened[i] == False][0]
    return 1 if person_choice == car else 0

for simulation in range(NO_OF_SIMULATIONS):
    award = always_switch_strategy()
    winning_car += 1 if award == CAR else 0
    winning_goat += 1 if award == GOAT else 0


probability_of_car = (winning_car/NO_OF_SIMULATIONS)*100
probability_of_goat = (winning_goat/NO_OF_SIMULATIONS)*100
print("WINNING A CAR:", str(probability_of_car) + "%")
print("WINNING A GOAT:", str(probability_of_goat) + "%")
