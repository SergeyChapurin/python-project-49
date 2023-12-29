from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_correct_answer():

    num_1 = randint(0, 100)
    num_2 = randint(0, 100)

    question = f'{num_1} {num_2}'
    correct_answer = str(gcd(num_1, num_2))

    return question, correct_answer
