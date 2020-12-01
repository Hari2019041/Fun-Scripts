import random

words = [
    "typewriter",
    "carpenter",
    "dancer",
    "printer",
    "drilling",
    "love",
    "wolf",
    "street"
]


def print_word(word, letters):
    for letter in word:
        if letter in letters:
            print("_ ", end="")
        else:
            print(letter, end=" ")
    print()


def play_game():
    word = random.choice(words)

    letters = []

    for letter in word:
        if letter not in letters:
            letters.append(letter)

    max_tries = 5
    tries = 0

    while len(letters) != 0 and tries < max_tries:
        print_word(word, letters)
        guess = input()
        if guess in letters:
            letters.remove(guess)
        else:
            tries += 1
        print("Failed Tries:", tries)

    print(word)


play_game()
