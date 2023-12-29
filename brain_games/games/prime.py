from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):

    if x < 2:
        return False

    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False

    return True


def get_question_and_correct_answer():

    question = randint(1, 100)
    correct_answer = "yes" if is_prime(question) else "no"

    return question, correct_answer
