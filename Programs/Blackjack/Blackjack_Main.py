# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:46:09 2019

@author: Zebs
"""

from Blackjack_Board import *

import ipdb

playingChar_main = 'Noone'

if __name__ == '__main__':

    #Game set up
    GAME = True
    board = Board()
    player = Player(100)
    dealer = Dealer(100)

    while GAME == True:

        board.reset()
        if GAME == False:
            break
        else:
            pass

        #CARD DRAW PHASE
        playingChar_main = player
        playingChar_main.bet()
        playingChar_main.draw(2)
        board.calc_score()

        playingChar_main = dealer
        playingChar_main.draw(2)
        playingChar_main.hide()
        board.calc_score()
        #End of CARD DRAW PHASE

        #show BOARD
        board.display()

        playingChar_main = player
###              
        playingChar_main.play()

        if playingChar_main.decision == 1:
            playingChar_main.draw()
            board.display()
            playingChar_main.check_loss()

        if board.loser_Board == "Noone":
            playingChar_main.decided = False
            playingChar_main.play()

        elif playingChar_main.decision == 2:
            playingChar_main.betted_in_Player = False

            playingChar_main.bet(playingChar_main.total_bet_in_Player)
            playingChar_main.draw()
            board.display()
            playingChar_main.check_loss()

        elif playingChar_main.decision == 3:
            pass

        playingChar_main.calc_score()

        board.display()

        board.check_loss()

        if board.loser_Board != "Noone":
            continue
        else:
            playingChar_main = dealer
            playingChar_main.play()
            play_result()
###