#!/usr/bin/env python3

import prompt
from random import randint


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Welcome to the Brain Games!")
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    i = 3
    while i > 0:
        num = randint(1, 100)
        print(f'Question: {num}')
        your_answer = prompt.string('Your answer: ')
        if num % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if your_answer == correct_answer:
            i = i-1
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
        if i == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()