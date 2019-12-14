# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:46:09 2019

@author: Zebs
"""

from Board import Board,delay

from CharBase import CharBase

from Player import Player
from Dealer import Dealer
###
import ipdb

class Main:
    """
    Lowest level class that processes and converts data between all classes.
    """
    
    def __init__(self):
        self.playing_char = None
        self.char_list = [player, dealer]
        self.loser = None
        
    def value_reset(self):

        if GAME == True:
            board.create_deck()
            board.generate_CARD_VALUE()
            self.loser = None
            
            player.hand = []
            player.decision = 0
            player.decided = False
            player.total_bet_in_Player = 0
            player.betted_in_Player = False
            try:
                del bet_amount_in_Player
            except UnboundLocalError:   #bet_amount_in_Player does not exist
                pass

            dealer.hand = []
            dealer.revealed = False

            print("\n \n \n \n \n")

        else:
            pass

    def check_game_over(self):
        """
        Checks if any characters are broke.
        """
        for names in self.char_list:
            if names.money_in_CharBase == 0:
                global GAME
                GAME = False

                print(f"{names.name} is broke. {names.name} loses!")
                
                break

    def display(self):
        """
        Outputs game interface.
        """
        print("------------------------------------- \n"
              f"Dealer's hand: {dealer.hand} \n"
              f"Dealer's score: {dealer.score1_in_CharBase} or {dealer.score2_in_CharBase} \n"
              f"Dealer's bank: ${dealer.money_in_CharBase}"
              "\n \n \n \n \n"
              f"Player's hand: {player.hand} \n"
              f"Player score: {player.score1_in_CharBase} or {player.score2_in_CharBase} \n"
              f"Player's bet: ${player.total_bet_in_Player} \n"
              f"Player's bank: ${player.money_in_CharBase}"
              "\n-------------------------------------")
        delay(3)

    def check_loss(self):
        """
        Checks if any character score is higher than 21, and if so, assigns them to self.loser.
        """
        for char in self.char_list:
            if type(char.score1_in_CharBase) is str:
                pass

            elif char.score1_in_CharBase > 21:

                print(f"{char.name}'s score is over 21!")

                self.loser = char

                delay()

    def game_result(self):
        """
        Checks self.loser and compares score values to see who lost and who won.
        Also adds and subtracts cash from characters according to that result.
        """
        if self.loser == None:
            if player.score1_in_CharBase > dealer.score1_in_CharBase:
                self.loser = dealer

            elif player.score1_in_CharBase < dealer.score1_in_CharBase:
                self.loser = player

            else:   #is a draw
                print("It's a draw!")
                player.money_in_CharBase += player.total_bet_in_Player
                print(f"{player.name} gets their bet, ${player.total_bet_in_Player} back!")

        if self.loser != None:
            index = self.char_list.index(self.loser)
            other_char = self.char_list[abs(index - 1)]

            if self.loser == player:
                dealer.money_in_CharBase += player.total_bet_in_Player

            if self.loser == dealer:
                print(f"{player.name} gets their bet, ${player.total_bet_in_Player} back!")
                player.money_in_CharBase += player.total_bet_in_Player*2
                dealer.money_in_CharBase -= player.total_bet_in_Player

            print(f"{self.loser.name} loses ${player.total_bet_in_Player}.")
            delay()
            print(f"{other_char.name} wins ${player.total_bet_in_Player}.")

    def draw_calc_display(self):
        """
        Draws card, calculates character score, displays interface, then check character if they should be a loser.
        """

        self.playing_char.draw_card()        
        self.playing_char.calc_score()
        self.display()
        self.check_loss()

    def turn_switch(self):
        """
        Unused feature at the moment.
        """

        while True:

            if self.playing_char == self.char_list[0]:
                self.playing_char = self.char_list[1]

                yield self.playing_char

            else:
                self.playing_char = self.char_list[0]

                yield self.playing_char

if __name__ == '__main__':
    #Object creation
    board = Board()
    player = Player(100)
    dealer = Dealer(100)
    main = Main()

    #GLOBAL VALUES
    GAME = True

    while GAME == True:

        main.check_game_over()
        main.value_reset()
        
        if GAME == False:
            break
        else:
            pass

        for char in main.char_list:
            print(f"{char.name} has ${char.money_in_CharBase}.")

            delay()

        #CARD DRAW PHASE
        main.playing_char = player

        main.playing_char.bet()
        main.playing_char.draw_card(2)
        main.playing_char.calc_score()

        main.playing_char = dealer

        main.playing_char.draw_card(2)
        main.playing_char.calc_score()
        main.playing_char.hide_card()
        #End of CARD DRAW PHASE

        #show BOARD
        main.display()

        main.playing_char = player             

        while main.playing_char == player:
            
            player.make_decision()
            
            if player.decision == 1:
                main.draw_calc_display()

                if main.loser == None:
                    player.decided = False
                    continue
                else:
                    break

            elif player.decision == 2:                
                player.betted_in_Player = False

                player.bet(player.total_bet_in_Player)
                main.draw_calc_display()
                break

            elif player.decision == 3:
                break

        if main.loser != None:
            main.game_result()
            continue

        main.playing_char = dealer

        dealer.reveal_card()
        dealer.calc_score()

        main.display()
        
        main.check_loss()

        while dealer.score1_in_CharBase < 17:                
            main.draw_calc_display()

        main.playing_char = None

        main.game_result()