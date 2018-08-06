# coding utf-8

import random


class UI(object):
    def __init__(self, ):
        self.stages = [
            "============     ",
            "||        |      ",
            "||        |      ",
            "||        0      ",
            "||       /|\     ",
            "||       / \     ",
            "||______________ ", ]
        self.states = ['win',
                       'game over',
                       'success try',
                       'wrong try']
        self.state = 'start'
        self.messages = {'game over': "Ты использовал все шансы. Игра окончена!",
                         'win': 'Ты выиграл! Кажется, в этот раз казнь отменяется :(',
                         'success try': 'Прошлый раз ты угадал, посмотрим, сможещь ли сейчас!',
                         'wrong try': 'Прошлый раз ты  не угадал, и на шаг ближе к виселице!'}
        self.title = """*** HANGMAN ***
                    'Добро пожаловать на казнь!\n'"""
        self.board = None
        self.wrong = 0

    def draw(self):
        print(self.title)
        for i in range(self.wrong):
            print(self.stages[i])
        print("\n")
        print(" ".join(self.board))
        if self.state in ['start', 'success try', 'wrong try']:
            print('Угадай спрятанное слово.')
        print(self.messages[self.state])


def load_words():
    with open('words.txt', 'r') as f:
        words = f.read()
    return words.split('\n')


def hangman():
    word = random.choice(load_words())
    rletters = list(word)
    wrong = 0

    ui = UI()
    ui.board = ['_'] * len(word)

    while wrong < len(ui.stages) - 1:
        ui.draw()
        msg = 'Введите букву: '
        char = input(msg)

        if char in rletters:
            ui.state = 'success try'
            cindex = rletters.index(char)
            ui.board[cindex] = char
            rletters[cindex] = '$'
        else:
            ui.state = 'wrong try'
            ui.wrong += 1
        if '_' not in ui.board:
            ui.state = 'win'
            break
    if ui.state != 'win':
        ui.state = 'game over'
        ui.draw()
        print('"Это было слово {} (Ха-ха-ха!)'.format(word.upper()))


if __name__ == '__main__':
    hangman()
