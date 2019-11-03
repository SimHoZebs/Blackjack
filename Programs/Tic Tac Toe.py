# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:06:57 2019

@author: simho
"""
from msvcrt import getch

def e2c(*word):
    if not bool(word):
        print(f"(Press Enter to {'continue'}...)")
    else:
        print(f"(Press Enter to {word[0]}...)")

    while not getch() == b'\r':
        continue

def debug(*word):
    global DEBUG_CHECK
    if DEBUG_CHECK == 0:
        pass
    else:
        print(word)

DEBUG_CHECK = 0

game_board = "7   8   9 \n4   5   6 \n1   2   3"

print("Welcome to a game of Tic Tac Toe!")
e2c()
print("In this version of Tic Tac Toe,"
      " the numpad will represent the board layout,"
      " like the following:")

print(game_board)

print("Pressing one of the numbers will"
      " place your stone on that position.")
e2c()
print("Player 1's stone will be repesnted with O,"
      " and player 2's with X.\n\nPlayer 1 starts first.")
e2c('start')

player = 1
game_over = 0

WIN_CONDITION = ['123', '456', '789', '147', '258', '369', '357', '159']
p1_stone = ''
p2_stone = ''
p1_win = 0
p2_win = 0

while game_over == 0:
    print(f'Player {player}')
    print(game_board)

    key_press = str(getch())[2]

    if key_press in game_board:
        if player == 1:
            p1_stone += key_press
            game_board = game_board.replace(key_press, 'O')
            print(game_board)
            player = 2
            debug('p1_stone:', p1_stone)
        else:
            p2_stone += key_press
            game_board = game_board.replace(key_press, 'X')
            print(game_board)
            player = 1
            debug('p2_stone:', p2_stone)
    else:
        print("Either the key you pressed is not a number,"
              " or you're trying to place a stone where there already is one.")

    for conditions in WIN_CONDITION:
        debug('Checking with', conditions)
        for num in conditions:
            debug('Checking for number:', num)
            if num in p1_stone:
                p1_win += 1
            elif num in p2_stone:
                p2_win += 1

            debug('p1_win:', p1_win)
            debug('p2_win:', p2_win)

        if p1_win < 3:
            debug('p1 does not win yet')
            p1_win = 0
        else:
            print('p1 won')
            break

        if p2_win < 3:
            p2_win = 0
        else:
            print('p2 won')
            break

    if p2_win or p1_win == 3:
        game_over = 1
