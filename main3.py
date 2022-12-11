ZERO = {
    'ноль': 0,
}
ONES = {
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
}

TWENTIES = {
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
}

TENS = {
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
}

HUNDREDS = {
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
}


def word_to_number(input_text):
    string_list = input_text.lower().strip().split()
    # проверка всех слов на правильность
    for word in string_list:
        if word in ONES or word in TWENTIES or word in TENS or word in HUNDREDS or word in ZERO:
            ...
        else:
            return f'Ошибка в слове {word}'

    number = 0
    if string_list[0] in HUNDREDS:
        number += HUNDREDS.get(string_list[0])
        if len(string_list) > 1:
            if string_list[1] in TENS:
                number += TENS.get(string_list[1])
                if len(string_list) > 2:
                    if string_list[2] in ONES:
                        number += ONES.get(string_list[2])
                    else:
                        return f'Ошибка в слове {string_list[2]}'
            elif string_list[1] in TWENTIES:
                number += TWENTIES.get(string_list[1])
                if len(string_list) > 2:
                    return f'Ошибка в слове {string_list[2]}'
            elif string_list[1] in ONES:
                number += ONES.get(string_list[1])
                if len(string_list) > 2:
                    return f'Ошибка в слове {string_list[2]}'
    elif string_list[0] in TENS:
        number += TENS.get(string_list[0])
        if len(string_list) > 1:
            if string_list[1] in ONES:
                number += ONES.get(string_list[1])
            else:
                return f'Ошибка в слове {string_list[1]}'
    elif string_list[0] in TWENTIES:
        number += TWENTIES.get(string_list[0])
        if len(string_list) > 1:
            return f'Ошибка в слове {string_list[1]}'
    elif string_list[0] in ONES:
        number += ONES.get(string_list[0])
        if len(string_list) > 1:
            return f'Ошибка в слове {string_list[1]}'
    return number



