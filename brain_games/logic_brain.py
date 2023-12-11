import prompt
rounds = 3


def logic_brain(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.start_message)
    i = 0
    while i < rounds:
        question, correct_answer = game.round()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == correct_answer:
            i = i + 1
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
        if i == rounds:
            print(f'Congratulations, {name}!')