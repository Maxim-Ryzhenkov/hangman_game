# coding utf-8

import random

stages = [
          "============     ",
          "||        |      ",
          "||        |      ",
          "||        0      ",
          "||       /|\     ",
          "||       / \     ",
          "||______________ ",]

game_over = "Ты использовал все шансы. Игра окончена!"
win_msg = 'Ты выиграл! Кажется, в этот раз казнь отменяется :('


def load_words():
    with open('words.txt', 'r') as f:
        words = f.read()
    return words.split('\n')


def draw_screen(wrong, board, win, fail, success_try=None):
    print('*** HANGMAN ***')
    print('Добро пожаловать на казнь!\n')
    for i in range(wrong):
        print(stages[i])
    print("\n")
    print(" ".join(board))
    if not win and not fail:
        print('Угадай спрятанное слово.')
    if success_try is True:
        print('Прошлый раз ты угадал, посмотрим, сможещь ли сейчас!')
    elif success_try is False:
        print('Прошлый раз ты  не угадал, и на шаг ближе к виселице!')
    elif win:
        print(win_msg)
    elif fail:
        print(game_over)
    else:
        pass


def hangman():
    word = random.choice(load_words())
    rletters = list(word)
    board = ['_'] * len(word)
    wrong = 0
    win = False
    fail = False
    success_try = None
    while wrong < len(stages) - 1:
        print('\n')
        draw_screen(wrong, board, win, fail, success_try)
        msg = 'Введите букву: '
        char = input(msg)
        if char in rletters:
            cindex = rletters.index(char)
            board[cindex] = char
            rletters[cindex] = '$'
            success_try = True
        else:
            wrong += 1
            success_try = False
        if '_' not in board:
            win = True
            draw_screen(wrong, board, win, fail)
            break
    if not win:
        fail = True
        draw_screen(len(stages), board, win, fail)
        print('"Это было слово {} (Ха-ха-ха!)'.format(word.upper()))

if __name__ == '__main__':
    hangman()
