from random import randint
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer():
    num = randint(1, 100)
    question = num
    correct_answer = "yes" if num % 2 == 0 else "no"
    return question, correct_answer
