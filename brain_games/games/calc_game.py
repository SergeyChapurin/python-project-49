from random import randint
from random import choice
BEGINNING = 'What is the result of the expression?'

def game_stage():
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    oper_list = ['+', '-', '*']
    oper = choice(oper_list)
    question = f'{num_1} {oper} {num_2}'
    if oper == '+':
        correct_answer = str(num_1 + num_2)
    elif oper == '-':
        correct_answer = str(num_1 - num_2)
    else:
        correct_answer = str(num_1 * num_2)
    return question, correct_answer