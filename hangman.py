from random import choice

words = {}
with open('dictionary.txt', 'r') as file:
    for word in file.readlines():
        if len(word) >= 6 and len(word) <= 11:
            words.append(word[0:-1].lower())


def print_word(word, letters):
    for letter in word:
        print('_ ', end='') if letter in letters else print(letter, end=' ')
    print()


def play_game():
    word = choice(words)

    letters = []

    for letter in word:
        letters.append(letter) if letter not in letters else ''

    MAX_TRIES = 5
    tries = 0

    while len(letters) != 0 and tries < MAX_TRIES:
        print_word(word, letters)
        guess = input()
        if guess in letters:
            letters.remove(guess)
        else:
            tries += 1
        print('Failed Tries:', tries)

    print(word)


play_game()
