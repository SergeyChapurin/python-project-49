from random import randint
BEGINNING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_stage():
    num = randint(2, 100)
    question = (f'Question: {num}')
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return question, correct_answer
