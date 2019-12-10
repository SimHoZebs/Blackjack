from Blackjack_CharBase import CharBase

from random import choice
from time import sleep

class Dealer(CharBase):
    def __init__(self, money):
        super().__init__(money)
        self.name = 'Dealer'
        self.socre1_hidden_in_Dealer = 0
        self.score2_in_hidden_in_Dealer = 0
        self.revealed = False

    def hide(self):
        self.hidden_card = choice(self.hand)
        self.hand.remove(self.hidden_card)
        self.hand.append("HIDDEN CARD")

        if card_value[self.hand[0]] == 'special':
            self.socre1_hidden_in_Dealer = 11
            self.score2_in_hidden_in_Dealer = 1

        else:
            self.socre1_hidden_in_Dealer = self.score2_in_hidden_in_Dealer = card_value[self.hand[0]]

        self.score1_in_CharBase = f"{self.socre1_hidden_in_Dealer} + x"
        self.score2_in_CharBase = f"{self.score2_in_hidden_in_Dealer} + x"

    def reveal(self):   #Swaps the hidden card with the actual card, revealing it.
        print("Revealing HIDDEN CARD...")
        sleep(1.4)

        self.hand.append(self.hidden_card)
        self.hand.remove("HIDDEN CARD")

        print(f"The HIDDEN CARD was a {self.hidden_card}!")
        sleep(1.4)
        self.calc_score()   #THIS IS TO CHANGE SCORE VALUE TO TRUE SCORE
        board.display()

    def play(self):
        if self.revealed == False:
            self.revealed = True
            self.reveal()

        if self.score1_in_CharBase >= 17:
            self.decision = 3
        else:
            self.decision = 1