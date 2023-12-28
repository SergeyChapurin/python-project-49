from random import randint
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_correct_answer():
    num = randint(2, 100)
    question = num
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return question, correct_answer
