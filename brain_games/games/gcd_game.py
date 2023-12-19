from random import randint
BEGINNING = 'Find the greatest common divisor of given numbers.'


def game_stage():
    num_1 = randint(0, 100)
    num_2 = randint(0, 100)
    question = f'{num_1} {num_2}'
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    correct_answer = str(num_1 + num_2)
    return question, correct_answer