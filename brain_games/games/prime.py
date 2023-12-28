from random import randint
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def get_question_and_correct_answer():
    num = randint(2, 100)
    question = num
    correct_answer = "yes" if is_prime(num) else "no"
    return question, correct_answer
