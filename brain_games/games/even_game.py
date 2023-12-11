from random import randint
start_message = 'Answer "yes" if the number is even, otherwise answer "no".'


def round():
    num = randint(1, 100)
    question = (f'Question: {num}')
    if num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer