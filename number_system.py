def digit(num, words):
    hundreds = words[num // 100]
    num = num % 100
    hn = hundreds + ' ' + 'Hundred '
    hn = '' if hundreds == '' else hn

    tens = words[int((num // 10) * 10)] + ' '
    num = num % 10
    ones = words[num]

    return hn + tens + ones


def english_language():
    words = {
        1: 'ONE',
        2: 'TWO',
        3: 'THREE',
        4: 'FOUR',
        5: 'FIVE',
        6: 'SIX',
        7: 'SEVEN',
        8: 'EIGHT',
        9: 'NINE',
        10: 'TEN',
        11: 'ELEVEN',
        12: 'TWELVE',
        13: 'THIRTEEN',
        14: 'FOURTEEN',
        15: 'FIFTEEN',
        16: 'SIXTEEN',
        17: 'SEVENTEEN',
        18: 'EIGHTEEN',
        19: 'NINETEEN',
        20: 'TWENTY',
        30: 'THIRTY',
        40: 'FORTY',
        50: 'FIFTY',
        60: 'SIXTY',
        70: 'SEVENTY',
        80: 'EIGHTY',
        90: 'NINETY',
        100: 'HUNDRED'
    }
    word_length = {}

    for key in words:
        word_length[key] = len(words[key])

    number_names = {}

    for i in range(1, 101):
        if i <= 20 or i in words.keys():
            number_names[i] = words[i]

        else:
            number_names[i] = words[(i // 10) * 10] + words[i % 10]

    no_of_steps = []
    steps_list = {}

    for i in range(1, 101):
        steps = 1
        no = i
        steps_list[i] = ''
        while (no != 4):
            steps_list[i] += str(no) + '->'
            steps += 1
            no = len(number_names[no])
        no_of_steps.append(steps)

        steps_list[i] += '4'

    print(steps_list)
    print(no_of_steps)


english_language()
