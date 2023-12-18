import prompt
ROUNDSCOUNT = 3


def play_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.BEGINNING)
    for win in range(0, ROUNDSCOUNT):
        question, correct_answer = game.game_stage()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        if your_answer != correct_answer:
            print(f"'{your_answer}' is wrong ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
        print('Correct!')
    if win == ROUNDSCOUNT - 1:        
        print(f'Congratulations, {name}!')