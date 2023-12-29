from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    start = randint(1, 50)
    step = randint(1, 10)
    len_prog = randint(7, 10)
    stop = start + step * len_prog

    progression = list(range(start, stop, step))
    hide_index = randint(0, len_prog - 1)

    correct_answer = str(progression[hide_index])
    progression[hide_index] = '..'
    question = " ".join(map(str, progression))

    return question, correct_answer
