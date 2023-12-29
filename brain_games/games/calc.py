from random import randint
from random import choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_correct_answer():
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*')
    ])

    question = f'{num_1} {operator} {num_2}'
    correct_answer = str(operation(num_1, num_2))

    return question, correct_answer
