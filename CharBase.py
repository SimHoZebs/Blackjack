from Board import Board,delay

from random import choice
from time import sleep
import ipdb

class CharBase:

    def __init__(self, money):
        self.money_in_CharBase = money
        self.hand = []
        self.hand_size_in_CharBase = len(self.hand)
        self.decision = 0
        self.score1_in_CharBase = 0     #SCORE VALUE FOR WHEN ACE == 11
        self.score2_in_CharBase = 0     #SCORE VALUE FOR WHEN ACE == 1

    def draw_card(self, amount=1):
        """
        Draws a random card from Board.deck. Repeat for amount.
        """
        for _ in range(amount):
            drawn_card = choice(Board.deck)
            Board.deck.remove(drawn_card)
            self.hand.append(drawn_card)

            if self.name == "Dealer" and len(self.hand) <= 2:
                print("Dealer draws a card.")

            else:
                print(f"{self.name} draws {drawn_card}.")

            delay(1.4)

    def calc_score(self):
        """
        Adds value of all cards in hand and assigns it to their scores.
        Score resets before each calc. Need to change it.
        """
        score1 = 0
        score2 = 0
        ace_in_hand = 0
        
        for cards in self.hand:
            try:
                score1 += Board.CARD_VALUE[cards]
            except TypeError:   #This occurs when the card in hand is an ACE.             
                ace_in_hand += 1
    
        score2 = score1

        if ace_in_hand == 1:
            score2 += 1

            if score1 >= 11:
                score1 += 1
            elif score1 < 11:
                score1 += 11

        elif ace_in_hand > 1:
            score1 += ace_in_hand
            score2 += ace_in_hand

        self.score1_in_CharBase = score1
        self.score2_in_CharBase = score2

    def bet_version6(self):
        pass