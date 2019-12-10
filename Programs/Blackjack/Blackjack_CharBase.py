from random import choice
from time import sleep

class CharBase:
    def __init__(self, money):
        self.money_in_CharBase = money
        self.hand = []
        self.decision = 0
        self.hand_size_in_CharBase = len(self.hand)
        self.score1_in_CharBase = 0     #SCORE VALUE FOR WHEN ACE == 11
        self.score2_in_CharBase = 0     #SCORE VALUE FOR WHEN ACE == 1

        global playingChar_main

    def draw(self, amount=1):
        cycle = 0

        while cycle != amount:
            drawn_card = choice(board.deck_Board)
            board.deck_Board.remove(drawn_card)
            self.hand.append(drawn_card)

            if self.name == "Dealer" and len(self.hand) <= 2:
                print("Dealer draws a card.")

            else:
                print(f"{self.name} draws {drawn_card}.")

            cycle += 1
            sleep(1.4)
    #Score resets before each calc. Need to change it.