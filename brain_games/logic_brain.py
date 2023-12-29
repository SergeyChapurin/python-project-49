import prompt


ROUNDSCOUNT = 3


def play_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.DESCRIPTION)

    for win in range(0, ROUNDSCOUNT):
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')

        if your_answer != correct_answer:
            print(f'"{your_answer}" is wrong ;(.\n'
                  f'Correct answer was "{correct_answer}".\n'
                  f"Let's try again, {name}!")
            return
        print('Correct!')

    print(f'Congratulations, {name}!')
