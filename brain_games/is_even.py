from random import randint
import prompt

def is_even():
    i = 3
    while i > 0:
        num = randint(1, 100)
        print(f'Question: {num}')
        your_answer = prompt.string('Your answer: ')
        print(f'Your answer: {your_answer}')
        if num % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if your_answer == correct_answer:
            i = i-1
            print('Correct!')
        else:
            print(f"{your_answer} is wrong ;(. Correct answer was {correct_answer}./n Let's try again")
            break
        if i == 0:
            print('Congratulations, Bill!')